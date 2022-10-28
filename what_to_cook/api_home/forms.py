from django.forms import ModelForm
from api_home.models import IngredientsModel
from django import forms
from . import models

class IngredientsForm(ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ["proteins","vegetables","legumes","starch","spices_and_herbs"]



