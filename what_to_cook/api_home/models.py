from tkinter import Widget
from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

PROTEIN_CHOICES =(
    (1, "Boeuf"),
    (2, "Veau"),
    (3, "Saumon"),
    (4, "Oeufs"),
)

VEGGIES_CHOICES =(
    (1, "Haricots Verts"),
    (2, "Brocoli"),
    (3, "Poivron"),
    (4, "Tomate"),
)

MY_CHOICES2 = ((1, 'Item title 2.1'),
               (2, 'Item title 2.2'),
               (3, 'Item title 2.3'),
               (4, 'Item title 2.4'),
               (5, 'Item title 2.5'))

class MyModel(models.Model):

    proteins = MultiSelectField(choices=PROTEIN_CHOICES,
                                 max_length=10)
    # veggies = MultiSelectField(choices=VEGGIES_CHOICES,
    #                              max_choices=3,
    #                              max_length=20)