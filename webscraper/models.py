from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    salary = models.CharField(max_length=250, null=True)
    remote = models.CharField(max_length=250, null=True)
    summary = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

    class Admin:
        pass
