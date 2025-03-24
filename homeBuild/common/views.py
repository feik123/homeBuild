from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from homeBuild.accounts.models import HomeOwnerProfile, ContractorProfile
from homeBuild.common.forms import CommentForm
from homeBuild.common.models import Like, Comment
from homeBuild.projects.models import Project

# Create your views here.
UserModel = get_user_model()

class HomePageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_type = None
        homeowner_profile = None
        contractor_profile = None

        if self.request.user.is_authenticated:
            # Check for homeowner profile
            try:
                homeowner_profile = HomeOwnerProfile.objects.get(user=self.request.user)
                profile_type = 'homeowner'
            except HomeOwnerProfile.DoesNotExist:
                pass  # If no profile exists, leave homeowner_profile as None

            # Check for contractor profile
            try:
                contractor_profile = ContractorProfile.objects.get(user=self.request.user)
                profile_type = 'contractor'
            except ContractorProfile.DoesNotExist:
                pass  # If no profile exists, leave contractor_profile as None

        context['profile_type'] = profile_type
        context['homeowner_profile'] = homeowner_profile
        context['contractor_profile'] = contractor_profile

        return context

@login_required
def likes_functionality(request, project_id: int):
    liked_object = Like.objects.filter(
        user=request.user,
        to_project_id=project_id,
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(user=request.user, to_project_id=project_id)
        like.save()


    return redirect(request.META['HTTP_REFERER'] + f'#{project_id}')

@login_required
def comments_functionality(request, project_id: int):
    if request.POST:
        project = Project.objects.get(pk=project_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_project_id = project.pk
            comment.user = request.user
            comment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{project_id}')