from django import forms

from homeBuild.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
        }

