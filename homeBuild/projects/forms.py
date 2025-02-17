from django import forms

from homeBuild.projects.models import Project


class ProjectBaseForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('photo', 'address', 'description')
        widgets = {
            'photo': forms.TextInput(attrs={'placeholder': 'Add photo'}),
            'address': forms.TextInput(attrs={'placeholder': 'Add address'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }

class ProjectAddForm(ProjectBaseForm):
    pass

class ProjectEditForm(ProjectBaseForm):
    pass
