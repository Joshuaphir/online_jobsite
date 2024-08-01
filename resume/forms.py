from django import forms
from . models import Resume

class UpResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user',)