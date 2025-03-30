from django import forms

from homeBuild.jobs.models import Job


class JobBaseForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['id']

class JobEditForm(JobBaseForm):
    pass

class JobDeleteForm(JobBaseForm):
    pass

