# Generated by Django 2.1 on 2018-10-26 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20181026_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='password',
        ),
    ]
