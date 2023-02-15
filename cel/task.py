from celery import shared_task

from django.core.mail import send_mail


@shared_task()
def send_mail_task(email_address, message):
    send_mail('Reminder', message, 'hillel@example.com', [email_address], fail_silently=False)
