from django.forms import ModelForm
from .models import Students, IngredientsModel
from django import forms




class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = {'name', 'section'}
       
        



class IngredientsForm(ModelForm):
    class Meta:
        model = IngredientsModel
        fields = {'proteins','veggies'}




        
