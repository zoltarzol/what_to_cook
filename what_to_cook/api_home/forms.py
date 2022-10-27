from django.forms import ModelForm
<<<<<<< HEAD
from .models import IngredientsModel
from django import forms




# class StudentsForm(ModelForm):
#     class Meta:
#         model = Students
#         fields = {'name', 'section'}
       
        


=======
from api_home.models import IngredientsModel
>>>>>>> 3cedef29d8c012cf98ffdac0c7bdc9d25e6e7677

class IngredientsForm(ModelForm):
    class Meta:
        model = IngredientsModel
<<<<<<< HEAD
        fields = {'proteins','veggies'}




        
=======
        fields = ["proteins","vegetables","legumes","starch","spices_and_herbs"]
>>>>>>> 3cedef29d8c012cf98ffdac0c7bdc9d25e6e7677
