# Generated by Django 2.1 on 2018-11-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0022_auto_20181116_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekendday',
            name='id',
        ),
        migrations.AlterField(
            model_name='weekendday',
            name='weekend_day',
            field=models.CharField(max_length=2, primary_key=True, serialize=False, unique=True),
        ),
    ]
