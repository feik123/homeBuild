from django import forms

from homeBuild.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['id']

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']

