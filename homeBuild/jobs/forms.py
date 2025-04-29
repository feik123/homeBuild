from django import forms

from homeBuild.jobs.models import Job


class JobBaseForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['id']


class JobAddForm(JobBaseForm):


    class Meta:
        model = Job
        exclude = ['id', 'homeowner', 'date_of_publication']


class JobEditForm(JobBaseForm):
    pass


class JobDeleteForm(JobBaseForm):
    pass
