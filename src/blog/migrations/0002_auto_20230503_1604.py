# Generated by Django 2.2 on 2023-05-03 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='updated',
        ),
    ]
