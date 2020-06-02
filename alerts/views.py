from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

import functions.alerts.emails.admin as email_admins
import functions.alerts.emails.user as email_users

# Create your views here.
def email_alerts(request):


    return render(request, 'alerts/email_alerts.html')


def new_user(request):
    email_admins.new_user_alert()
    return redirect('alerts:email_alerts')


def job_notification(request):
    email_users.jobs_notification_alert()
    return redirect('alerts:email_alerts')
