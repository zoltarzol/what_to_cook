from django.http import HttpResponse
from django.shortcuts import render, redirect


from . import forms
from api_home.forms import Userrs
from django.shortcuts import redirect  

def base (request):
    return render (request, 'api_home/base.html')

def aask (request):
    if request.method=="POST": #si l'user a rempli, si des données sont postées#
        form= Userrs(request.POST).save()#pr enregistrer les données; si données enregistrées: on crée un formulaire d'enregistrement des données#
        return redirect('/asking')
    else:
        form= Userrs()# = si aps de données envoyées= on soumet le questionnaire à l'user#

    return render(request,'pages_main/ask.html', {'form':form, })



def create_recipe(request):
    form = IngredientsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(api_call.findrecipe(api_call.ingredients_from_UI,0.7)["RecipeName"])
            print(dict(form.cleaned_data))
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form })


dico_1 = {"recette": 'oeuf à la coque', "ingredients": ['oeufs', 'fromage', 'radis noir'], "instructions": ["1:mettez de lhuile sur le feu"," 2:mettez 2 oeufs entier dans la poele", "3: faire cuire à feu doux durant 2min", "4: mettre dans une assiette", "5: parsemez de fromage"]
}




def recipe_rslt (request):
    
    # for key, values in dico_1.items():
    #     print( key)
    #     print()
    #     if(isinstance(values, list)):
    #         for value in values:
    #             print(value)
    #     else:
    #         print(values)
    #         print()

   
    print(dico_1)
    return render(request, 'pages_main/final_recipe.html',context = dico_1)

    {recette}
    {{dic_a}}
#def aask(request):
 #   if request.method == 'POST':
 #       form = UserForm(request.POST)
  #      if form.is_valid():
   #         user=form.save()

    #        return redirect('user-detail', user.id)

   # else:
    #    form = UserForm()

      #  return render(request, 'api_home/ask.html',
     #       {'form': form})

#def user_list(request):  # renommer la fonction de vue
 #  user = User.objects.all()
  # return render(request,

   #        {'users': user})

#def user_detail(request, id):
 # user = User.objects.get(id=id)  
  #return render(request,
     #     'myapp/User_detail.html',
   #       {'user': user}) 

#def page_home(request):
 #   return render(request, 'pages_main/home.html')


#def user_create(request):
 #   if request.method == 'POST':
  #      form = UserForm(request.POST)
   #     if form.is_valid():
            # créer une nouvelle « User » et la sauvegarder dans la db
    #        user = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
     #       return redirect('user-detail', user.id)

  #  else:
   #     form = UserForm()

    #    return render(request,
   #         'pages_main/ask.html',
     #       {'form': form})





#"def user_list(request):  
 #  users = Connecti.objects.all()
  # return render(request,
 #          'pages_main/ask.html',  
   #        {'users': users})

#def user_detail(request, id):
 # user = User.objects.get(id=id)  
  #return render(request,
  #        'pages_main/ask.html',
   #       {'user': user})

