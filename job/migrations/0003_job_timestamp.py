# Generated by Django 4.2.13 on 2024-05-21 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 5, 21, 19, 11, 45, 835549, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
