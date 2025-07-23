from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email-ID', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Feedback', 'class': 'form-control', 'rows': 4})
        }

