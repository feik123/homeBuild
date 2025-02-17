from django.urls import path

from homeBuild.projects.views import ProjectAdd

urlpatterns = [
    path('add/', ProjectAdd.as_view(), name='add'),
]