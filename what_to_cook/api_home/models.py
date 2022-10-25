from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms




# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )


class Students(models.Model):
    name = models.TextField(max_length = 800)
    section = models.TextField(max_length = 800)

    def __str__(self):
        return self.name, self.section




class ProteinForm(forms.Form):
    PROTEIN_CHOICES =(
    ("boef", "Beef"),
    ("2", "Veal"),
    ("3", "Salman"),
    ("4", "Eggs"),
     )
    title = forms.MultipleChoiceField(choices = PROTEIN_CHOICES, widget=forms.CheckboxSelectMultiple())
    section = models.TextField(max_length = 800)

    def __str__(self):
        return self.name, self.section
    