from django.urls import path

from homeBuild.common import views
from homeBuild.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('comments/<int:project_id>/', views.comments_functionality, name='comments'),
    path('like/<int:project_id>/', views.likes_functionality, name='likes'),
]