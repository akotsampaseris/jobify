# Generated by Django 3.0.6 on 2020-05-11 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobinator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobinator',
            options={'ordering': ['created_at']},
        ),
    ]
