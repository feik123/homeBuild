from django.urls import path

from homeBuild.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]