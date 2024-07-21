from django.shortcuts import render

# Create your views here.
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.serializers import serialize

from rest_framework import generics
from .serializers import *
from rest_framework.permissions import  AllowAny
from api.models import *
from rest_framework import viewsets

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class ListUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    
class FileUploadView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = []

class FileListView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = []