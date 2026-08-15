from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control mb-10',
                'rows': '5',
                'placeholder': 'Write your comment...',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Write your comment...'",
            }),
        }
