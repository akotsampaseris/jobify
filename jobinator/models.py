from django.db import models
from django.utils import timezone

# Create your models here.
class Jobinator(models.Model):
    position = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    active   = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['created_at']

    class Admin:
        pass
