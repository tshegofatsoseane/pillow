# Generated by Django 5.0.6 on 2024-06-09 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlords', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landlord',
            name='name',
        ),
    ]
