from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from .functions import csv_to_dict

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

ingredients_list_temp = csv_to_dict("/home/cedric/Documents/what_to_cook/what_to_cook/api_home/ingredients_list.csv")
proteins = ingredients_list_temp['Proteins']
cpt = 1
protein_choices = []
for protein_ingredient in proteins:
    protein_choices.append([cpt,protein_ingredient])
    cpt += 1


PROTEIN_CHOICES = tuple(protein_choices)

vegetables = ingredients_list_temp['Vegetables']
cpt = 1
vegetables_choices = []
for vegetables_ingredient in vegetables:
    vegetables_choices.append([cpt,vegetables_ingredient])
    cpt += 1

VEGETABLES_CHOICES = tuple(vegetables_choices)

class IngredientsModel(models.Model):

    proteins = MultiSelectField(choices=PROTEIN_CHOICES,
                                #  max_choices=2,
                                 max_length=500,
                                 null=True,
                                 blank=True)
    veggies = MultiSelectField(choices=VEGETABLES_CHOICES,
                                #  max_choices=3,
                                 max_length=500,
                                 null=True,
                                 blank=True)