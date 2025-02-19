from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.accounts.models import ContractorProfile

UserModel = get_user_model()

class Project(models.Model):
    photo = models.URLField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100,null=True, blank=True)
    profile = models.ForeignKey(
        ContractorProfile,
        on_delete=models.CASCADE
    )

