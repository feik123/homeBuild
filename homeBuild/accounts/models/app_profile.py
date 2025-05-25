from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.common.utils import geocode_address

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.address and (not self.latitude or not self.longitude):
            self.latitude, self.longitude = geocode_address(self.address)

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class HomeOwnerProfile(Profile):

    def __str__(self):
        return f"Homeowner profile for {self.user}"


class JobCategory(models.Model):
    name = models.CharField(
        max_length=30,
        choices=(
            ('renovation', 'Renovation'),
            ('maintenance', 'Maintenance'),
            ('landscaping', 'Landscaping'),
            ('electrical', 'Electrical'),
            ('plumbing', 'Plumbing'),
            ('cleaning', 'Cleaning'),
            ('other', 'Other'),
        ),
        default='other'
    )

    def __str__(self):
        return self.name



class ContractorProfile(Profile):


    job_categories = models.ManyToManyField(JobCategory, blank=True)

    experience = models.SmallIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Contractor profile for {self.user}"
