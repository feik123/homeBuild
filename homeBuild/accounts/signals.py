from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, HomeOwnerProfile, ContractorProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.profile_type == 'homeOwner':
            HomeOwnerProfile.objects.create(user=instance)
        else:
            ContractorProfile.objects.create(user=instance)

