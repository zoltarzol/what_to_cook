from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField




# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )
