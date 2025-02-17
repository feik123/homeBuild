from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from homeBuild.projects.forms import ProjectAddForm
from homeBuild.projects.models import Project


class ProjectAdd(CreateView, LoginRequiredMixin):
    model = Project
    form_class = ProjectAddForm
    template_name = 'projects/project-add.html'
    success_url = reverse_lazy('index')
    # TO DO redirect to profile-details

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            project = form.save(commit=False)
            project.user = self.request.user
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('login'))

    def get_context_data(self, **kwargs):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )