# Generated by Django 2.1 on 2018-11-23 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0003_auto_20181123_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 11, 59, 35, 151193), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'PENDING'), (2, 'APPROVED'), (3, 'REJECTED'), (4, 'DELETED'), (5, 'CANCELLED')], null=True),
        ),
    ]
