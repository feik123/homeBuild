# Generated by Django 4.2.17 on 2025-03-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_jobcategory_remove_contractorprofile_job_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='profile_type',
            field=models.CharField(choices=[('homeowner', 'Homeowner'), ('contractor', 'Contractor')], default='homeowner', max_length=20),
        ),
    ]
