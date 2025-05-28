from django.urls import path

from homeBuild.jobs.views import CreateJobView, JobListView, NearbyJobsView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='job-create'),
    path('', JobListView.as_view(), name='job-list'),
    path('nearby/', NearbyJobsView.as_view(), name='job-nearby'),
]