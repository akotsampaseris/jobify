# Generated by Django 3.0.6 on 2020-05-05 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0002_auto_20200505_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='created_at',
        ),
    ]
