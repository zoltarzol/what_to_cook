
from django import forms 
from api_home.models import Ask

# listings/forms.py

from django import forms

#class ConnectiForm(forms.Form):
    #class Meta:
       # name = forms.CharField(required=False)
        #email = forms.EmailField()
        #message = forms.CharField(max_length=1000)#

class Userrs(forms.ModelForm):
    class Meta:
        model = Ask
        fields = '__all__'


