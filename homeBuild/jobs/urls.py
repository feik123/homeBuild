from django.urls import path

from homeBuild.jobs.views import CreateJobView, JobListView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='job-create'),
    path('job-list/', JobListView.as_view(), name='job-list'),
]