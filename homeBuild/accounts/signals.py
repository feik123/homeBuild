from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, HomeOwnerProfile, ContractorProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Automatically create a HomeOwnerProfile or ContractorProfile based on user type (if necessary)
@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Example of creating a HomeOwnerProfile, you can change it to ContractorProfile if needed
        HomeOwnerProfile.objects.create(user=instance)  # Or ContractorProfile based on your logic

@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):  # This checks if the profile exists
        instance.profile.save()
