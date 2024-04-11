# test_email.py

# Import Django modules
import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Configure Django settings
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'scooter_bike_ecommerce.settings')
django.setup()

# Set up email parameters
subject = 'Test Email'
message = 'This is a test email sent from Django.'
from_email = settings.DEFAULT_FROM_EMAIL
to_email = ['enganwar100@hotmail.com']  # Replace with recipient email address

try:
    # Send the email
    send_mail(subject, message, from_email, to_email)
    print("Test email sent successfully!")
except Exception as e:
    print("An error occurred while sending the test email:")
    print(e)


# Send test email
send_mail(subject, message, from_email, to_email)
