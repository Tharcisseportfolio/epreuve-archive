from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import *
from .models import *

"""
*****************Description****************

@variable starts with _, it is a relatable field model to be use it in the post 
example:
    _grade : It is a primary key for the model grade which is related to the model
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class TestSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = Test
        fields = ['id', 'test','link','course', 'section', 'year']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = instance.course.course  # Assuming 'name' is the field in Course model
        representation['section'] = instance.section.section  # Assuming 'name' is the field in Section model
        return representation

class CourseSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=True)
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'grade','course','section', 'tests']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['section'] = instance.section.section
        
        return representation

class SectionSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'section', 'courses']

class SectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['section']


#Email sending serialisers
class SendEmailSerializer(serializers.ModelSerializer):
        class Meta:
            model = SendEmail
            fields = ['id','subject', 'email', 'message', 'sent_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id','subject', 'email', 'message', 'received_at']