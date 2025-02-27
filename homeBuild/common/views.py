from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from homeBuild.common.forms import CommentForm
from homeBuild.common.models import Like, Comment
from homeBuild.projects.models import Project

# Create your views here.
UserModel = get_user_model()

class HomePageView(TemplateView):
    template_name = 'common/index.html'

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