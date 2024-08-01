from django import forms
from . models import Company

class UpCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)