from django.urls import path

from . import views

urlpatterns = [
    path('my-jobs', views.my_jobs, name="my_jobs"),
    path('create-job', views.create, name="create_job"),
    path('activate-job/<int:id>', views.activate, name="activate_job"),
    path('delete-job/<int:id>', views.delete, name="delete_job"),
]
