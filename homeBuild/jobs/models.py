from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.accounts.models import JobCategory
from homeBuild.common.utils import geocode_address
from homeBuild.jobs.managers import JobManager
from homeBuild.photos.models import Photo

# Create your models here.

UserModel = get_user_model()

class Job(models.Model):
    homeowner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    job_category = models.ForeignKey(
        to=JobCategory,
        on_delete=models.SET_DEFAULT,
        default='other',
        null=True,
        blank=True
    )
    location = models.CharField(max_length=255,)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    date_of_publication = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.location and (not self.latitude or not self.longitude):
            self.latitude, self.longitude = geocode_address(self.location)

        super().save(*args, **kwargs)

    objects = JobManager()

    def __str__(self):
        return self.title

class JobPhoto(models.Model):
    job = models.ForeignKey(
        to=Job,
        on_delete=models.CASCADE,

        related_name='photos'
    )
    image = models.ImageField(upload_to='job_photos/')

    def __str__(self):
        return f"Photo for job: {self.job.title}"