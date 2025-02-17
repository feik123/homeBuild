from lib2to3.fixes.fix_input import context

from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from homeBuild.accounts.forms import AppUserCreationForm, ProfileEditForm
from homeBuild.accounts.models import HomeOwnerProfile
from homeBuild.projects.models import Project

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'accounts/client-login.html'

class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/client-register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response



class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            profile = self.object.profile  # Access the related profile
        except UserModel.profile.RelatedObjectDoesNotExist:
            profile = None  # If no profile exists, set it to None or handle accordingly

        if profile:
            projects = Project.objects.filter(profile=profile)
        else:
            projects = []

        context['projects'] = projects
        context['profile'] = profile

        return context

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