from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from homeBuild.accounts.forms import AppUserCreationForm, ProfileEditForm
from homeBuild.accounts.models import Profile, ContractorProfile, HomeOwnerProfile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/client-login.html'

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/client-register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response

class ProfileEditView(UpdateView):
    model = HomeOwnerProfile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )