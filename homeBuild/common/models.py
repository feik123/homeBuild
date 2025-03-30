from django.contrib.auth import get_user_model
from django.db import models

from homeBuild.accounts.models import JobCategory
from homeBuild.photos.models import Photo
from homeBuild.projects.models import Project
from homeBuild.jobs.models import Job

UserModel = get_user_model()

class Comment(models.Model):
    text = models.TextField(max_length=200)
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    to_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    to_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )



class ContractorApplication(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE, related_name='applications')
    contractor = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='applications')
    message = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contractor} - {self.job.title}"


class Message(models.Model):
    sender = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name='received_messages')
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # To track if the message has been read

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} for {self.job.title}"
