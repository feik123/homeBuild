# Generated by Django 4.2.17 on 2025-04-28 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='photo',
        ),
        migrations.CreateModel(
            name='JobPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='jobs.job')),
            ],
        ),
    ]
