# Generated by Django 4.2.13 on 2024-05-31 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_edu_qualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliedjob',
            old_name='company',
            new_name='job',
        ),
    ]
