# Generated by Django 4.2.13 on 2024-05-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_rename_experience_job_company_overview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='edu_qualification',
            field=models.TextField(default="Bachelor's Degrees", max_length=100),
            preserve_default=False,
        ),
    ]
