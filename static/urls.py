from django.urls import path

from . import views

app_name = 'static'
urlpatterns = [
    path('', views.home, name="home"),
]
