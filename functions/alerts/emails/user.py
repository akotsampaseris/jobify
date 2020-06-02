import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .helpers.content import read_content, send_message

template = os.path.dirname(__file__) + '/templates/user/'

from_email = '"Jobify | Find your dream job" <a.kotsampaseris@technologic.gr>'
to = ['a.kotsampaseris@gmail.com']

@receiver(post_save, sender=User)
def new_user_alert(sender, instance, created, **kwargs):
    subject = 'Welcome to Jobify!'
    content = read_content(template, 'new_user')

    send_message(subject, content, from_email, to)
    

def jobs_notification_alert():
    subject = 'New jobs found!'
    content = read_content(template, 'jobs_notification')

    send_message(subject, content, from_email, to)
