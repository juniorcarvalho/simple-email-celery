from celery import task
from django.core.mail import send_mail


@task
def send_simple_email(subject, body, email_from, emails_to):
    return send_mail(subject, body, email_from, emails_to, fail_silently=False)
