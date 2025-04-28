from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')

    date_of_publication = models.DateField(
        auto_now=True,
    )


    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return f"Photo by {self.user}"