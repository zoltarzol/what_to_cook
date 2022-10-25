from django import forms
from api_home.models import Ingredients

class IngredientsForm(forms.Form):
	PROTEIN_CHOICES =(
		("1", "Beef"),
		("2", "Veal"),
		("3", "Salmon"),
		("4", "Eggs"),
	)

	VEGGIES_CHOICES =(
		("1", "Beef"),
		("2", "Veal"),
		("3", "Salmon"),
		("4", "Eggs"),
	)

	proteins = forms.MultipleChoiceField(choices = PROTEIN_CHOICES, widget=forms.CheckboxSelectMultiple())
	vegetables = forms.MultipleChoiceField(choices = PROTEIN_CHOICES, widget=forms.CheckboxSelectMultiple())

	class Meta:
		print("je suis passé par là")
		model = Ingredients
		fields = '__all__'




# class ProteinForm(forms.Form):
	
