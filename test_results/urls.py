from django.urls import path

from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name="index"),
    path('select-websites', views.select_websites, name="select_websites"),
    path('create-website', views.create_website, name="create_website"),
    path('update-website/<int:id>', views.update_website, name="update_website"),
    path('delete-website/<int:id>', views.delete_website, name="delete_website")
]
