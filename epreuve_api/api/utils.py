import os,sys
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epreuve_api.settings')
application = get_wsgi_application() # type: ignore
from api.models import *


def filter_by_section(self, model):
    organiseData= {}

    model_data = model.objects.all()

    for epreuve_data in model_data:
        if epreuve_data.section not in organiseData:
            organiseData[epreuve_data.section] = []
        organiseData[epreuve_data.section].append(epreuve_data)

    return organiseData


def filter_by_course(self, model):
    organiseData= {}

    model_data = model.objects.all()

    for epreuve_data in model_data:
        if epreuve_data.course not in organiseData:
            organiseData[epreuve_data.course] = []
        organiseData[epreuve_data.course].append(epreuve_data.tests.all())

    return organiseData





