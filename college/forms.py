from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'Bank', 'Capital_Amount', 'Interest', 'message',)


