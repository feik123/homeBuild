from django.contrib.auth.views import LogoutView
from django.urls import path, include

from homeBuild.accounts import views
from homeBuild.accounts.views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),

        # path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]