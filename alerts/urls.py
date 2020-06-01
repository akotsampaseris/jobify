from django.urls import path

from . import views

app_name = 'alerts'
urlpatterns = [
    path('email-alert', views.email_alert, name="email_alert"),
]
