from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.projects.models import Project

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

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='project_photos',
        null=True,
        blank=True
    )

    job = models.ForeignKey(
        'common.Job',
        on_delete=models.CASCADE,
        related_name='job_photos',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Photo by {self.user} for {'Job' if self.job else 'Project'} {self.job.id if self.job else self.project.id} "