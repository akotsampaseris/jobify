from django.urls import path

from . import views

app_name = 'alerts'
urlpatterns = [
    path('email-alerts', views.email_alerts, name="email_alerts"),
    path('new-user', views.new_user, name="new_user"),
    path('job-notifications', views.job_notification, name="job_notification"),
]
