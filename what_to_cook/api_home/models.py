from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
<<<<<<< HEAD
from .functions import csv_to_dict


=======
from .functions import ingredients_csv_to_dict, split_ingredients_dict_by_category
>>>>>>> 3cedef29d8c012cf98ffdac0c7bdc9d25e6e7677

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

<<<<<<< HEAD
ingredients_list_temp = csv_to_dict("/home/ousfia/snap/what_to_cook/what_to_cook/what_to_cook/api_home/ingredients_list.csv")
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

=======
ingredients_list = ingredients_csv_to_dict("api_home/ingredients_list.csv")

PROTEIN_CHOICES = split_ingredients_dict_by_category(ingredients_list,'Proteins')
VEGETABLES_CHOICES = split_ingredients_dict_by_category(ingredients_list,'Vegetables')
LEGUMES_CHOICES = split_ingredients_dict_by_category(ingredients_list,'Legumes')
STARCH_CHOICES = split_ingredients_dict_by_category(ingredients_list,'Starch')
SPICES_AND_HERBS_CHOICES = split_ingredients_dict_by_category(ingredients_list,'Spices / Herbs')

CHOICES = [PROTEIN_CHOICES,VEGETABLES_CHOICES,LEGUMES_CHOICES,STARCH_CHOICES,SPICES_AND_HERBS_CHOICES]

class IngredientsModel(models.Model):
>>>>>>> 3cedef29d8c012cf98ffdac0c7bdc9d25e6e7677
    proteins = MultiSelectField(choices=PROTEIN_CHOICES,
                                #  max_choices=2,
                                 max_length=500,
                                 null=True,
                                 blank=True)
<<<<<<< HEAD
    veggies = MultiSelectField(choices=VEGETABLES_CHOICES,
=======
    vegetables = MultiSelectField(choices=VEGETABLES_CHOICES,
                                #  max_choices=3,
                                 max_length=500,
                                 null=True,
                                 blank=True)
    legumes = MultiSelectField(choices=LEGUMES_CHOICES,
                                #  max_choices=2,
                                 max_length=500,
                                 null=True,
                                 blank=True)
    starch = MultiSelectField(choices=STARCH_CHOICES,
                                #  max_choices=3,
                                 max_length=500,
                                 null=True,
                                 blank=True)
    spices_and_herbs = MultiSelectField(choices=SPICES_AND_HERBS_CHOICES,
>>>>>>> 3cedef29d8c012cf98ffdac0c7bdc9d25e6e7677
                                #  max_choices=3,
                                 max_length=500,
                                 null=True,
                                 blank=True)