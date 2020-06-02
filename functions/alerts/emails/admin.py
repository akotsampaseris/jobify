import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .helpers.content import read_content, send_message

template = os.path.dirname(__file__) + '/templates/admin/'

subject_prefix = '[Jobify]'

from_email = '"Jobify | Find your dream job" <a.kotsampaseris@technologic.gr>'
to = ['a.kotsampaseris@gmail.com']

@receiver(post_save, sender=User)
def new_user_alert(sender, instance, created, **kwargs):
    if created:
        subject = 'New user!'

        content = read_content(template, 'new_user')

        send_message(subject_prefix, subject, content, from_email, to)
