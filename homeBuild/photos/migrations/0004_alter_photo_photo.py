# Generated by Django 4.2.17 on 2025-02-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_project_alter_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
