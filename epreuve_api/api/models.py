from django.db import models
from django.contrib.auth.models import User

class SendEmail(models.Model):

    class Meta:
        ordering =['sent_at']

    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class ContactMessage(models.Model):
    class Meta:
        ordering = ['received_at']

    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Section(models.Model):
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.section

class Course(models.Model):
    Grade_Choices = (
        ('3','3ème Post Fondemental'),
        ('9','9è Fondemental')
    )
    grade = models.CharField(max_length=40,choices=Grade_Choices,null=True)

    course = models.CharField(max_length=100)
    section = models.ForeignKey(Section, related_name='courses', on_delete=models.CASCADE)


    def __str__(self):
        return self.course

class Test(models.Model):

    DOC_TYPES = (
        ('Q', 'Questionnaire'),
        ('A', 'Answers'),
    )

    course = models.ForeignKey(Course, related_name='tests', on_delete=models.CASCADE,null=True)
    section = models.ForeignKey(Section, related_name='tests', on_delete=models.CASCADE)
    test = models.CharField(max_length=100)
    link = models.FileField(upload_to='documents/',default='')
    type = models.CharField(max_length=1, choices=DOC_TYPES,default='Q')
    year = models.DateField()

    def __str__(self):
        return self.test