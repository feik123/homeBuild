from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from homeBuild.accounts.models import Profile, HomeOwnerProfile, ContractorProfile

UserModel = get_user_model()

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class HomeOwnerProfileEditForm(forms.ModelForm):
    class Meta:
        model = HomeOwnerProfile
        exclude = ('user',)

class ContractorProfileEditForm(forms.ModelForm):
    class Meta:
        model = ContractorProfile
        exclude = ('user',)