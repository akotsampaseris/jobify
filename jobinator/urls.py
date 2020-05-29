from django.urls import path

from . import views

app_name = 'jobinator'
urlpatterns = [
    path('my-jobs', views.my_jobs, name="my_jobs"),
    path('create-job', views.create, name="create_job"),
    path('activate-job/<int:id>', views.activate, name="activate_job"),
    path('deactivate-job/<int:id>', views.deactivate, name="deactivate_job"),
    path('delete-job/<int:id>', views.delete, name="delete_job"),
]
