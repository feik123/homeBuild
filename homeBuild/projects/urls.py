from django.urls import path, include

from homeBuild.projects.views import ProjectAdd, ProjectDetails

urlpatterns = [
    path('add/', ProjectAdd.as_view(), name='add'),
    path('project/<int:pk>/', include([
        path('', ProjectDetails.as_view(), name='project-details'),

    ]
    ))
]