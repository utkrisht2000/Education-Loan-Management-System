from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'bank', 'message', 'GOV_Status', 'GOV_Bank', 'GOV_Capital_Amount', 'GOV_Interest',
        	'SBI_Status', 'SBI_Capital_Amount', 'SBI_Interest', 
    		'PNB_Status', 'PNB_Capital_Amount', 'PNB_Interest',
    		 'Axis_Status', 'Axis_Capital_Amount', 'Axis_Interest',
    		  'HDFC_Status', 'HDFC_Capital_Amount', 'HDFC_Interest',
    		  'BOB_Status', 'BOB_Capital_Amount', 'BOB_Interest',
    		  'Canara_Status', 'Canara_Capital_Amount', 'Canara_Interest',
    		  'ICICI_Status', 'ICICI_Capital_Amount', 'ICICI_Interest',
    		  'Kotak_Status', 'Kotak_Capital_Amount', 'Kotak_Interest',
    		  'DCB_Status', 'DCB_Capital_Amount', 'DCB_Interest',
    		  'IDBI_Status', 'IDBI_Capital_Amount', 'IDBI_Interest',
    		  'Andhra_Status', 'Andhra_Capital_Amount', 'Andhra_Interest',
    		  'Federal_Status', 'Federal_Capital_Amount', 'Federal_Interest',
    		  'IndusInd_Status', 'IndusInd_Capital_Amount', 'IndusInd_Interest',
    		  'Karnataka_Status', 'Karnataka_Capital_Amount', 'Karnataka_Interest',
    		  'City_Status', 'City_Capital_Amount', 'City_Interest',
    		  'UCO_Status', 'UCO_Capital_Amount', 'UCO_Interest',
    		  'KVB_Status', 'KVB_Capital_Amount', 'KVB_Interest',
    		  'RBL_Status', 'RBL_Capital_Amount', 'RBL_Interest',
    		  'YES_Status', 'YES_Capital_Amount', 'YES_Interest',
    		  'Union_Status', 'Union_Capital_Amount', 'Union_Interest',
    		  'Auxillo_Status', 'Auxillo_Capital_Amount', 'Auxillo_Interest',
    		  'Avanse_Status', 'Avanse_Capital_Amount', 'Avanse_Interest',
    		  'Gyan_Status', 'Gyan_Capital_Amount', 'Gyan_Interest',
    		  'Student_Status', 'Student_Capital_Amount', 'Student_Interest',
    		  )


