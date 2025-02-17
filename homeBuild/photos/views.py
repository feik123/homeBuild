from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from homeBuild.photos.forms import PhotoAddForm
from homeBuild.photos.models import Photo
from homeBuild.projects.models import Project


class PhotoAddPage(LoginRequiredMixin ,CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('login')

        photo = form.save(commit=False)
        # Automatically set the user to the currently logged-in user
        photo.user = self.request.user

        # Get the project from the URL parameter and assign it to the photo
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        photo.project = project

        return super().form_valid(form)
