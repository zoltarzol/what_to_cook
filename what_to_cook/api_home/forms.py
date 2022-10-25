from django import forms
from api_home.models import Ingredients

class IngredientsForm(forms.Form):
	PROTEIN_CHOICES =(
		("Beef", "Boeuf"),
		("Veal", "Veau"),
		("Salmon", "Saumon"),
		("Eggs", "Oeufs"),
	)

	VEGGIES_CHOICES =(
		("Grean Beans", "Haricots Verts"),
		("Broccoli", "Brocoli"),
		("Bell Pepper", "Poivron"),
		("Tomato", "Tomate"),
	)

	proteins = forms.MultipleChoiceField(choices = PROTEIN_CHOICES, widget=forms.CheckboxSelectMultiple())
	vegetables = forms.MultipleChoiceField(choices = PROTEIN_CHOICES, widget=forms.CheckboxSelectMultiple())

	class Meta:
		model = Ingredients
		fields = '__all__'


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [‘name’, ‘date’, ‘members’]
    name = forms.CharField()
    date = forms.DateInput()
    members = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple