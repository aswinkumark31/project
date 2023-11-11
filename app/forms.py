from django import forms
from . models import *

class Todo_form(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'