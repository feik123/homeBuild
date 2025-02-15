from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
UserModel = get_user_model()

class HomePageView(TemplateView):
    template_name = 'common/index.html'