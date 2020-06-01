from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
]
