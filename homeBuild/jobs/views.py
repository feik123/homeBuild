from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from homeBuild.jobs.forms import JobAddForm
from homeBuild.jobs.models import Job, JobPhoto


class CreateJobView(View):
    model = Job
    form_class = JobAddForm
    template_name = 'jobs/create.html'
    success_url = reverse_lazy('job-list')

    def get_profile_type(self):
        return self.request.user.profile_type

    def dispatch(self, request, *args, **kwargs):
        profile_type = self.get_profile_type()

        if profile_type != 'homeowner':
            return HttpResponseForbidden("You must be a home owner to post this job")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.homeowner = self.request.user
        response =  super().form_valid(form)

        for file in self.request.FILES.get('files'):
            JobPhoto.objects.create(job=self.object, image=file)

        return response

class JobListView(View):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'