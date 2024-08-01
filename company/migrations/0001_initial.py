# Generated by Django 5.0.4 on 2024-05-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('est_date', models.PositiveIntegerField(blank=True, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('headQuaters', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
