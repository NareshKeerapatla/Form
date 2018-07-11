from django import forms

from .models import ModelClass

class FormClass(forms.ModelForm):
    class Meta:
        model=ModelClass
        fields='__all__'
