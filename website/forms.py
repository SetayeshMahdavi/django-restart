from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter email address',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'common-textarea form-control',
                'placeholder': 'Enter Messege',
            }),
        }