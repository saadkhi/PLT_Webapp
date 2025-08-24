from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name', 'age', 'email', 'education_level', 'last_institute',
            'github_link', 'linkedin_link', 'resume', 'referral_source'
        ]
