from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import  AllowAny
from api.models import *
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.views import APIView

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
    def post(self):
        return self
    
    def delete(self):
        return self
    
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
 
