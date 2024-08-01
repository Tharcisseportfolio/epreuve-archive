from django.contrib.auth.models import User
from django.urls import get_resolver
from rest_framework import generics
from rest_framework.permissions import  AllowAny
from django.urls import get_resolver
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

from .serializers import *
from api.models import *


class SendEmailViewSet(viewsets.ModelViewSet):
    queryset = SendEmail.objects.all()
    serializer_class = SendEmailSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer) # save the data to the database...

            
            subject = serializer.validated_data['subject'] #the email subject
            email = serializer.validated_data['email'] # the email address we setup notification.epreuve@gmail.com
            message = serializer.validated_data['message'] # the message we want to send to clients 

            
            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            headers = self.get_success_headers(serializer.data)
            return Response({'message':'Email sent successfully'},serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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

class EndpointListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        urlconf = get_resolver().url_patterns
        endpoints = self.get_urls(urlconf)
        return Response(endpoints, status=status.HTTP_200_OK)

    def get_urls(self, urlpatterns, parent_pattern=''):
        endpoints = []
        for pattern in urlpatterns:
            if hasattr(pattern, 'url_patterns'):
                endpoints += self.get_urls(pattern.url_patterns, parent_pattern + pattern.pattern.regex.pattern)
            else:
                url = parent_pattern + pattern.pattern.regex.pattern
                name = pattern.name or ''
                if 'admin/' not in url:  # Exclude the admin endpoint
                    endpoints.append({'url': url, 'name': name})
        return endpoints
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ListUserView(generics.ListAPIView):
    query = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_queryset(self):
        users = User.objects.all()
        return users
    
class GradeView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = []

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = []

class EpreuveView(viewsets.ModelViewSet):
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = []

class EpreuveListView(generics.ListAPIView):
    query = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = []

    def get_queryset(self):
        epreuves = Epreuve.objects.all()
        return epreuves
    
class ExetatViewSet(viewsets.ModelViewSet):
    queryset = Exetat.objects.all()
    serializer_class = ExetatSerializer
    permission_classes = []

class FileUploadView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = []

class FileListView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = []

class NinthGradeCoursesView(generics.ListAPIView):
    query = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = []

    def get_queryset(self):

        results = Grade.objects.filter(name='9')
        for grade in results:
            ninth_courses = Course.objects.filter(grade=grade.id)
            if ninth_courses:
                for course in ninth_courses:
                    print("The night grade :",course.name)
                return ninth_courses

class ThirdGradeCoursesView(generics.ListAPIView):
    query = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = []

    def get_queryset(self):

        results = Grade.objects.filter(name='3')
        for grade in results:
            third_courses = Course.objects.filter(grade=grade.id)
            if third_courses:
                for course in third_courses:
                    print("The thirst post fundemental grade :",course.name)
                return third_courses
 
