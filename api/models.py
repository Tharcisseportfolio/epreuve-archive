from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    class Meta:
        ordering =['name']

    CHOICES = (
        ('3', '3ème Post Fondamental(Finalistes)'),
        ('9', '9ème Fondemental'),
    )
    name = models.CharField(max_length=255, choices=CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Section(models.Model):
    class Meta:
        ordering =['name']
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    class Meta:
        ordering =['name']

    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='courses')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=4000, null=True, default="")

    def __str__(self):
        return self.name

class Epreuve(models.Model):
    class Meta:
        ordering =['date']
        
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='epreuves')
    name = models.CharField(max_length=255)
    date = models.DateField()  # when the epreuve was released

    def __str__(self):
        return f'{self.name} ({self.course})'

class Exetat(models.Model):
    class Meta:
        ordering =['date']
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exetats')
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.course})'

class File(models.Model):
    class Meta:
        ordering =['name']
    DOC_TYPES = (
        ('Q', 'Questionnaire'),
        ('A', 'Answers'),
    )
    
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE, related_name='files')
    type = models.CharField(max_length=1, choices=DOC_TYPES)
    name = models.CharField(max_length=200, default="2002")
    link = models.FileField(upload_to='documents/', default='')

    def __str__(self):
        return f'{self.name} ({self.get_type_display()})'

# class Grade(models.Model):
#     Choices = (
#         ('3', '3ème Post Fondamental(Finalistes)'),
#         ('9', '9ème Fondemental'),
#     )
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,choices=Choices)

#     def __str__(self):
#         return self.name

# class Section(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     id = models.AutoField(primary_key=True)
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#     grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     tag = models.CharField(max_length=4000,null=True,default="")

#     def __str__(self):
#         return self.name

# class Epreuve(models.Model):
#     id = models.AutoField(primary_key=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     section = models.ForeignKey(Section,on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     date = models.DateField() #when the epreuve was released

#     def __str__(self):
#         return self.name

# class Exetat(models.Model):
#     id = models.AutoField(primary_key=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     section = models.ForeignKey(Section,on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     date = models.DateField()

#     def __str__(self):
#         return self.name
    
# class File(models.Model):

#     DOC_TYPES = (
#         ('Q', 'Questionnaire'),
#         ('A', 'Answers'),
#     )
    
#     id = models.AutoField(primary_key=True)
#     epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)
#     type = models.CharField(max_length=1, choices=DOC_TYPES)
#     name = models.CharField(max_length=200,default="2002")
#     link = models.FileField(upload_to='documents/',default='')

#     def __str__(self):
#         return f'{self.name}'
    

