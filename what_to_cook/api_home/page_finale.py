dico_1 = {"recette": 'oeuf à la coque', "ingredients": ['oeufs', 'fromage', 'radis noir'], "instructions": ["mettez de lhuile sur le feu"," 2:mettez 2 oeufs entier dans la poele", "3: faire cuire à feu doux durant 2min", "4: mettre dans une assiette", "5: parsemez de fromage"]
}

print (dico_1 ["ingredients"])
print()

for key, values in dico_1.items():
    print( key)
    print()
    if(isinstance(values, list)):
        for value in values:
            print(value)
            print()
    else:
        print(values)

#recette=dico_1[1]
#ingre=dico_1[2]
#etapes=dico_1[3]

for key, values in dico_1.items():
    print( key[1])
    if(isinstance(values, list)):
        for value in values:
            print(value)
            print()
    else:
        print(values)