# Generated by Django 4.2.17 on 2025-02-16 12:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_contractorprofile_job_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorprofile',
            name='job_categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('renovation', 'Renovation'), ('maintenance', 'Maintenance'), ('landscaping', 'Landscaping'), ('electrical', 'Electrical'), ('plumbing', 'Plumbing'), ('cleaning', 'Cleaning'), ('other', 'Other')], default='other', max_length=30), blank=True, default=['Other'], size=None),
        ),
    ]
