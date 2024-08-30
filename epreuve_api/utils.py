import os,sys
import json
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
basedir = ""
sys.path.append(basedir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epreuve_api.settings')
application = get_wsgi_application() # type: ignore
from api.models import *
from api.serializers import TestSerializer
class DataRetrival:

    def __init__(self) -> None:
        pass

    def filter_by_section(self, model):
        organiseData= {}

        model_data = model.objects.all()

        for epreuve_data in model_data:
            if epreuve_data.section not in organiseData:
                section = epreuve_data.section
                # print(section)
                organiseData[section] = []
            organiseData[section].append(epreuve_data)

        return organiseData
    

    def filter_by_course(self, model):
        organiseData= {}

        model_data = model.objects.all()

        for epreuve_data in model_data:
            if epreuve_data.course not in organiseData:
                organiseData[epreuve_data.course] = []
            organiseData[epreuve_data.course].append(epreuve_data.tests.all())

        return organiseData
    
# retrieval = DataRetrival()

# course_data = retrieval.filter_by_course(Course)
# section_data = retrieval.filter_by_section(Test)

# for section, tests in section_data.items():
#     section_name = section.section
#     serialized_tests = TestSerializer(tests, many=True).data
#     serialized_data[section_name] = serialized_tests

# print(section_data)
# serializer = TestSerializer(section_data, many=True)
# print(serializer)
# print(json.dumps(section_data, indent=4))

# for i,data in enumerate(course_data):
#     for j in range(len(course_data[data])):
#         course = course_data[data][j].course
#         tests = course_data[data][j].tests.all()




