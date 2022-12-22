from django import forms
from .models import DataLoad

class DataLoadingForm(forms.ModelForm):

    class Meta:
        model = DataLoad
        fields = ['data', 'userid']