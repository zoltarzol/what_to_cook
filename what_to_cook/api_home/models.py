from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

class Ingredients(models.Model):
    # proteins = []
    # vegetables = []
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    members = models.ManyToManyField(Member)