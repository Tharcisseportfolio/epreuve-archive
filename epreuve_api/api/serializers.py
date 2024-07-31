from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class EndpointSerializer(serializers.Serializer):
    url = serializers.CharField()
    name = serializers.CharField()
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'tag', 'grade', 'section']
        
    section = SectionSerializer(read_only=True)
    grade = GradeSerializer(read_only=True)

    

class EpreuveSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Epreuve
        fields = ['id', 'name','link', 'type','date', 'course']
        

class ExetatSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Exetat
        fields = ['id', 'name','link', 'type','date', 'course']
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"



    