from django.shortcuts import get_object_or_404
from django.views import View

from homeBuild.accounts.models import HomeOwnerProfile, ContractorProfile


class DynamicProfileMixin(View):

    def get_model(self):
        profile_type = self.kwargs.get('profile_type')

        if profile_type == 'homeowner':
            return HomeOwnerProfile
        elif profile_type == 'contractor':
            return ContractorProfile
        else:
            raise ValueError('Invalid profile type specified in the URL')


    def get_form_class(self):
        profile_type = self.kwargs.get('profile_type')

        if profile_type == 'homeowner':
            return HomeOwnerProfile
        elif profile_type == 'contractor':
            return ContractorProfile
        else:
            raise ValueError('Invalid profile type specified in the URL')

    def get_object(self, queryset=None):

        model = self.get_model()
        return get_object_or_404(model, pk=self.kwargs.get('pk'))