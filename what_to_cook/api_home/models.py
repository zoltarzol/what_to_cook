from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )

#class Ask (models.Model):
    #class meta:
        #name= models.CharField(max_length=100),
        #surname=models.CharField(max_length=50),
        #annee=models.DateField(),



class Ask(models.Model):
        SALADE='sl'
        POIVRON ='pvr'
        TOMATE ='tmt'
        CHAMPIGNON ='cpn'
        AGNEAU='ag'
        DINDE ='din'
        POULET ='pou'
        BOEUF ='bo'
        CHOIX_ALIMENTS = [
         (SALADE, 'salade'),
         (POIVRON, 'poivron'),
         (TOMATE, 'tomate'),
         (CHAMPIGNON, 'champignon'),]
        CHOIX_VIANDES = [
         (AGNEAU, 'agneau'),
         (DINDE, 'dinde'),
         (POULET, 'poulet'),
         (BOEUF, 'boeuf'),
    ]
        legume_toute = models.CharField(
        max_length=3,
        choices=CHOIX_ALIMENTS,
        default=SALADE,
    )


        de_la_viande= models.CharField(
        max_length=3,
        choices=CHOIX_VIANDES,
        default=AGNEAU,
    )