from django.test import TestCase

# Create your tests here.

import unittest 
from api_home.functions import split_ingredients_dict_by_category

# Create your tests here.

class test_ingredients_func(unittest.TestCase):

     def test_proteins_vegetables(self):

        self.assertEqual(split_ingredients_dict_by_category({"Féculents":["Pain","Pâtes","Pommes de Terre", "Riz"], "Légumes":["Carotte", "Brocoli"]}, "Légumes"), ([1, 'Carotte'], [2, 'Brocoli']))
        self.assertEqual(split_ingredients_dict_by_category({"Proteins":["Beef","Chicken","Cod"],"Legumes":["Lentils", "Navy bean"]}, "Proteins"), ("Beef","Chicken", "Cod"))
    #erreur attendue par rapport au format de réponse non conforme


    def verify_if_tuple (self):
        self.assertIsInstance(split_ingredients_dict_by_category({"Féculents":["Pain","Pâtes","Pommes de Terre", "Riz"], "Légumes":["Carotte", "Brocoli"]}, "Légumes"), (dict))

    #vérifie que résultat est bien un tuple