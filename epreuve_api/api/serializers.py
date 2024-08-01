from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

"""
*****************Description****************

@variable starts with _, it is a relatable field model to be use it in the post 
example:
    _grade : It is a primary key for the model grade which is related to the model
"""
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
    section = SectionSerializer(read_only=True)
    grade = GradeSerializer(read_only=True)
    
    #the _grade is the primary key for grade and course models
    # the _section is the primary key for grade and course models
    
    _section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), source='section', write_only=True)
    _grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all(), source='grade', write_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name',  '_grade','_section','tag', 'grade', 'section']

    

class EpreuveSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    _course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)
    class Meta:
        model = Epreuve
        fields = ['id', 'name','_course','link', 'type','date', 'course']
        

class ExetatSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    _course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)
    class Meta:
        model = Exetat
        fields = ['id', 'name','link', 'type','date', 'course']
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


#Email sending serialisers
class SendEmailSerializer(serializers.ModelSerializer):
        class Meta:
            model = SendEmail
            fields = ['id','subject', 'email', 'message', 'sent_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id','subject', 'email', 'message', 'received_at']