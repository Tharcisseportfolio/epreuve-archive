from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=4000,null=True,default="")

    def __str__(self):
        return self.name

class Epreuve(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField() #when the epreuve was released

    def __str__(self):
        return self.name

class Exetat(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class File(models.Model):

    DOC_TYPES = (
        ('Q', 'Questionnaire'),
        ('A', 'Answers'),
    )
    
    id = models.AutoField(primary_key=True)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=DOC_TYPES)
    name = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
    
