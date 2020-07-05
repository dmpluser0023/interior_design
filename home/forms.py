from django import forms
from .models import Quote

class Quate_form(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('name','email','message')