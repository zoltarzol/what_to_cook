from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from .functions import PROTEIN_CHOICES,VEGETABLES_CHOICES,LEGUMES_CHOICES,STARCH_CHOICES,SPICES_AND_HERBS_CHOICES

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

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