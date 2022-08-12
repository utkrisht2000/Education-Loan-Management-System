from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'bank', 'message', 'SBI_Status', 'SBI_Capital_Amount', 'SBI_Interest', 
    		'PNB_Status', 'PNB_Capital_Amount', 'PNB_Interest', 'Axis_Status', 
    		'Axis_Capital_Amount', 'Axis_Interest', 'HDFC_Status',
    		 'HDFC_Capital_Amount', 'HDFC_Interest',)


