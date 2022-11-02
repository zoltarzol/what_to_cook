from django.shortcuts import render
from .forms import IngredientsForm
from .functions import ingredients_full_list, find_recipe
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

@login_required
def create_recipe(request):
    print("REQUEST: ",request)
    form = IngredientsForm(request.POST)
    selected_ingredients =[]
    if request.method == "POST":
        if form.is_valid():
            print("FORM.DATA: ",form.data)
            form.save()
            print("INGREDIENT CHOICES: ",ingredients_full_list)
            print("FORM.CLEANED_DATA: ",form.cleaned_data)
            for cat,ingredient_idx_list in form.cleaned_data.items():
                for ingredient_idx in ingredient_idx_list:
                    if cat in ingredients_full_list.keys():
                        selected_ingredients.append(ingredients_full_list[cat][int(ingredient_idx)-1].lower())

            print("selected_ingredients: ",selected_ingredients)
            find_recipe(selected_ingredients)
        return render(request, 'pages_main/cedric.html', {'form': form, 'ingredients_full_list': ingredients_full_list })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form, 'ingredients_full_list': ingredients_full_list })

@login_required
def recipe_rslt (request):   
    return render(request, 'pages_main/final_recipe.html', context = recette)

class SignupPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'