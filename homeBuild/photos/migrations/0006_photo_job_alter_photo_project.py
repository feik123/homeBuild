# Generated by Django 4.2.17 on 2025-03-13 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_message'),
        ('projects', '0003_project_profile'),
        ('photos', '0005_alter_photo_project_alter_photo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_photos', to='common.job'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_photos', to='projects.project'),
        ),
    ]
