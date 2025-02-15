from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(upload_to='')
    description = models.TextField(
        blank=True,
        null=True,
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )