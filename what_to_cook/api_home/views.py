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

