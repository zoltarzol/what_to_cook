from django.shortcuts import render
from .forms import IngredientsForm
from . import functions


def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

def create_recipe(request):
    form = IngredientsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(functions.findrecipe(functions.ingredients_from_UI)["RecipeName"])
            print(dict(form.cleaned_data))
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form })

