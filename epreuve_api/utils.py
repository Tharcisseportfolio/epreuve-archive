import os,sys
from django.core.wsgi import get_wsgi_application
# Add the project directory to the Python path
sys.path.append('/Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epreuve_api.settings')
application = get_wsgi_application() # type: ignore
from tests.models import *


