# Generated by Django 4.2.17 on 2025-05-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_photo_jobphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobphoto',
            name='image',
            field=models.ImageField(upload_to='job_photos/'),
        ),
    ]
