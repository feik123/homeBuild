from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.projects.models import Project

UserModel = get_user_model()

class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    to_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )

