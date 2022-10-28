from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from .functions import ingredients_csv_to_dict, split_ingredients_dict_by_category

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

ingredients_list = ingredients_csv_to_dict("api_home/ingredients_list.csv")

# ingredients_list_copy = {}

# for i in range(5):
#     ingredients_list_copy = list(ingredients_list.keys())[i])

PROTEIN_CHOICES = split_ingredients_dict_by_category(ingredients_list,'proteins')
VEGETABLES_CHOICES = split_ingredients_dict_by_category(ingredients_list,'vegetables')
LEGUMES_CHOICES = split_ingredients_dict_by_category(ingredients_list,'legumes')
STARCH_CHOICES = split_ingredients_dict_by_category(ingredients_list,'starch')
SPICES_AND_HERBS_CHOICES = split_ingredients_dict_by_category(ingredients_list,'spices_and_herbs')

CHOICES = [PROTEIN_CHOICES,VEGETABLES_CHOICES,LEGUMES_CHOICES,STARCH_CHOICES,SPICES_AND_HERBS_CHOICES]

class IngredientsModel(models.Model):
    proteins = MultiSelectField(choices=PROTEIN_CHOICES,
                                #  max_choices=2,
                                 max_length=500,
                                 null=True,
                                 blank=True)
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
                                #  max_choices=3,
                                 max_length=500,
                                 null=True,
                                 blank=True)