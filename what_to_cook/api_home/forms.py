from django.forms import ModelForm
from api_home.models import IngredientsModel, TestModel
from api_home.forms import UserCreationForm

class IngredientsForm(ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ["proteins","vegetables","legumes","starch","spices_and_herbs"]

class TestForm(ModelForm):
    class Meta:
        model = TestModel
        fields = ["resultat"]




class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email", "password1", "password2")