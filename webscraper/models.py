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


class Website(models.Model):
    element_choices = [
        ('', ''),
        ('div', 'div'),
        ('a', 'a'),
        ('p', 'p'),
        ('span', 'span'),
        ('h1', 'h1'),
        ('h2', 'h2'),
        ('h3', 'h3')
    ]
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    query_prefix = models.CharField(max_length=250, null=True)
    position_query = models.CharField(max_length=250)
    location_query = models.CharField(max_length=250)
    postings_element = models.CharField(max_length=10,
                                        choices=element_choices,
                                        default='')
    postings_class_or_id = models.CharField(max_length=250)
    posting_url_element = models.CharField(max_length=10,
                                        choices=element_choices,
                                        default='')
    posting_url_class_or_id = models.CharField(max_length=250)
    posting_title_element = models.CharField(max_length=10,
                                        choices=element_choices,
                                        default='')
    posting_title_class_or_id = models.CharField(max_length=250)
    posting_company_element = models.CharField(max_length=10,
                                        choices=element_choices,
                                        default='')
    posting_company_class_or_id = models.CharField(max_length=250)
    posting_location_element = models.CharField(max_length=10,
                                        choices=element_choices,
                                        default='')
    posting_location_class_or_id = models.CharField(max_length=250)
