# Generated by Django 3.2.12 on 2022-06-17 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 14, 16, 23, 331744, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='subject',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 14, 16, 23, 331744, tzinfo=utc)),
        ),
    ]
