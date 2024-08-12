import json
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from django.db.models import Q
from epreuve_api import settings

from .models import *
from django.core.mail import send_mail, EmailMessage
from .serializers import *

from api.utils import *


class SendEmailViewSet(viewsets.ModelViewSet):
    queryset = SendEmail.objects.all()
    serializer_class = SendEmailSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        # Example email sending logic
        send_mail(
            subject=serializer.validated_data['subject'],
            message=serializer.validated_data['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[serializer.validated_data['email']]
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        return Response({'message': 'This endpoint is for sending contact messages via POST requests.'}, status=status.HTTP_200_OK)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer) # save the data to the database...
            
            subject = serializer.validated_data['subject']  # the email subject
            email = serializer.validated_data['email']  # the client's email address
            message = serializer.validated_data['message']  # the message from the client

            print("The email is :",email)
            # Compose email with reply-to header
            email_message = EmailMessage(
                subject, #subject
                message, #message
                email,  #from email
                [settings.EMAIL_HOST_USER],  # to email
                headers={'Reply-To': email}  # Set the client's email as the reply-to
            )
            email_message.send(fail_silently=False)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        return Response({'message': 'This endpoint is for sending contact messages via POST requests.'}, status=status.HTTP_200_OK)

  
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = []
    
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = []

    @action(detail=False, methods=['get'], url_path='(?P<query>[^/.]+)')
    def search_sections(self, request, query):
        sections = Section.objects.filter(section__iexact=query)
        if not sections.exists():
            sections = Section.objects.filter(section__icontains=query)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['get'], url_path='(?P<name>[^/.]+)/(?P<course_name>[^/.]+)')
    def tests_by_course(self, request, name, course_name):
        try:
            section = Section.objects.get(section__icontains=name)
            courses = Course.objects.filter(course__icontains=course_name, section=section)
            if courses.count() == 0:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
            elif courses.count() == 1:
                course = courses.first()
                serializer = CourseSerializer(course)
            else:
                serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except Section.DoesNotExist:
            return Response({'error': 'Section not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'], url_path='(?P<name>[^/.]+)/(?P<course_name>[^/.]+)/(?P<test>[^/.]+)')
    def get_test(self, request, name, course_name, test):
        search_query = test.lower()
        if search_query == 'test' or search_query == 'epreuves':
            course = Course.objects.filter(course__icontains=course_name).first()
            tests = Test.objects.filter(course__course__icontains=course_name)
            if not tests.exists():
                return Response({'error': f"No test fot {course}"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data)
        return Response({'error': 'Test not found'}, status=status.HTTP_404_NOT_FOUND)
        
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

    @action(detail=False, methods=['get'], url_path='(?P<query>[^/.]+)')
    def search_courses(self, request, query):
        courses = Course.objects.filter(course__iexact=query)
        if not courses.exists():
            query_words = query.split()
            q_objects = Q()
            for word in query_words:
                q_objects |= Q(course__icontains=word)
            courses = Course.objects.filter(q_objects).distinct()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = []

    @action(detail=False, methods=['get'], url_path='(?P<query>[^/.]+)')
    def search_tests(self, request, query):
        tests = Test.objects.filter(test__iexact=query)
        if not tests.exists():
            query_words = query.split()
            q_objects = Q()
            for word in query_words:
                q_objects |= Q(test__icontains=word) | Q(course__course__icontains=word) | Q(section__section__icontains=word)
            tests = Test.objects.filter(q_objects).distinct()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
    

class SectionViewList(viewsets.ViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializer
    permission_classes = []
    def list(self, request):
        queryset = Section.objects.all()
        for query in queryset:
            print(query)

        serializer = SectionListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Section.objects.all()
        section = get_object_or_404(queryset, pk=pk)
        serializer = SectionListSerializer(section)
        return Response(serializer.data)
    
