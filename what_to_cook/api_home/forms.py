from django.forms import ModelForm
from api_home.models import MyModel

class MyForm(ModelForm):
    class Meta:
        model = MyModel
        fields = {"proteins"}