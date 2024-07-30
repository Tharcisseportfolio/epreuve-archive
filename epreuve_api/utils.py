"""
- Testing the api to be able to use it for our frontend
- Testing especially the relationships

"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epreuve_api.settings')
application = get_wsgi_application() # type: ignore
from api.models import *

#get grades

class TestApi:

    def __init__(self):
        pass

    def getGrades(self,model):
        grades = model.objects.all()
        return grades
    def getCourses(self,model):
        courses = model.objects.all()
        return courses
    def getSections(self,model):
        sections = model.objects.all()
        return sections
    def getEpreuves(self,model):
        epreuves = model.objects.all()
        return epreuves
    def getFiles(self,model):
        files = model.objects.all()
        return files


test = TestApi()

# tests = [test.getGrades(Grade),
# test.getCourses(Course),
# test.getSections(Section),
# test.getEpreuves(Epreuve),
# test.getFiles(File),
# ]

# for tests in tests:
#     print(f"\n*****************{tests.model}***************")
#     for test in tests:
#         print(test)
    
class TestRelations:

    def __init__(self) -> None:
        pass

    def getCoursesByGrade(self,grade_level):
        courses = Course.objects.filter(grade=grade_level)
        return courses
    
    def getCoursesBySection(self):
        sections = Section.objects.all()
        

        for section in sections:
            
            courses = Course.objects.filter(section=section)
            print(f"Course {courses.first()} in section {section} ")
            return courses
    def getEpreuveByCourse(self):
        courses = Course.objects.all()
        for course in courses:
            
            epreuve = Epreuve.objects.filter(course=course)
            print(f"The Epreuve {epreuve} in the course {course} in section {Section.objects.filter(course=course)}")
            return epreuve

    def getFileByEpreuve(self):
        epreuves = Epreuve.objects.all()
        for epreuve in epreuves:
            return File.objects.filter(epreuve=epreuve)




relation = TestRelations()

relations = [relation.getCoursesByGrade('3'),relation.getCoursesBySection(),
             relation.getEpreuveByCourse(),relation.getFileByEpreuve(),
             ]


for fun in relations:
    print(f"..................{fun.model}.............")
    print(fun)





