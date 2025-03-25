from lib2to3.fixes.fix_input import context

from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView

from homeBuild.accounts.forms import AppUserCreationForm, HomeOwnerProfileEditForm, \
    ContractorProfileEditForm
from homeBuild.accounts.models import HomeOwnerProfile, ContractorProfile
from homeBuild.common.forms import CommentForm
from homeBuild.common.models import Like
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
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.object  # The user whose profile is being viewed

        # get ContractorProfile
        profile = ContractorProfile.objects.filter(user=user).first()


        # Fetch the projects related to the profile
        projects = Project.objects.filter(profile=profile) if profile else []

        current_user = self.request.user if self.request.user.is_authenticated else None

        for project in projects:
            project.has_liked = Like.objects.filter(user=current_user, to_project=project).exists()
            project.likes_count = Like.objects.filter(to_project=project).count()

        context['projects'] = projects
        context['profile'] = profile
        context['comment_form'] = CommentForm()

        return context


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'accounts/profile-edit-page.html'

    def get_profile_type(self):

        profile_type = self.request.user.profile_type
        print(f"Profile Type: {profile_type}")  # Print it for debugging
        return profile_type

    def get_model(self):
        """Dynamically choose the model based on the profile_type of the logged-in user."""
        profile_type = self.get_profile_type()

        # Map profile_type to the appropriate model
        if profile_type == 'homeowner':
            return HomeOwnerProfile
        elif profile_type == 'contractor':
            return ContractorProfile
        else:
            raise ValueError("Invalid profile type specified")

    def get_form_class(self):
        """Dynamically choose the form class based on the profile_type of the logged-in user."""
        profile_type = self.get_profile_type()

        # Map profile_type to the appropriate form class
        if profile_type == 'homeowner':
            return HomeOwnerProfileEditForm
        elif profile_type == 'contractor':
            return ContractorProfileEditForm
        else:
            raise ValueError("Invalid profile type specified")

    def get_object(self, queryset=None):
        """
        Override to dynamically return the correct profile type.
        We get the model dynamically using `get_model()` and fetch the object accordingly.
        """
        model = self.get_model()  # Dynamically fetch the model
        print(f"The Model is: {model}")
        return get_object_or_404(model, pk=self.kwargs.get('pk'))


    def get_success_url(self):
        """Redirect to the profile details page after successfully updating."""
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk},
        )

    def test_func(self):
        profile = self.get_object()
        print(f"The profile is {profile}")
        return self.request.user == profile.user