from django import forms

from homeBuild.jobs.models import Job


class JobBaseForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['id']

class JobAddForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'job_category', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'job_category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.HiddenInput()
        }

class JobEditForm(JobBaseForm):
    pass


class JobDeleteForm(JobBaseForm):
    pass

class JobsListForm(JobBaseForm):
    pass

