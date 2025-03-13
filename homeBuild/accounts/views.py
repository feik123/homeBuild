from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from homeBuild.accounts.forms import AppUserCreationForm, ProfileEditForm
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