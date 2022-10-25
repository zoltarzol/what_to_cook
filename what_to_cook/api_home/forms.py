from django.forms import ModelForm
from .models import Students, ProteinForm
from django import forms




class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = {'name', 'section'}
       
        



class test(forms.Form):
    class Meta:
        model =ProteinForm
        fields = {'section'}



        
