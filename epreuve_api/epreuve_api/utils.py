import os,sys
import django
from django.core.mail import send_mail
from django.conf import settings
sys.path.append('/Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epreuve_api.settings")
django.setup()

def send_test_email():
    send_mail(
        'Test Subject',
        'This is a test message.',
        settings.EMAIL_HOST_USER,[
        settings.RECIPIENT_ADDRESS],
        fail_silently=False,
    )
    
if __name__ == "__main__":
    send_test_email()