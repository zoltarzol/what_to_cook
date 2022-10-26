from dataclasses import fields
from django import forms
from api_home.models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["proteins"]