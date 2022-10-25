from django.shortcuts import render
from .forms import IngredientsForm
# Create your views here.

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

def cedric(request):
    context = {}
    context['form'] = IngredientsForm(request.POST or None)
    if request.method == 'POST':
        print(context['form'])
        return render(request,'pages_main/cedric.html',context)
    else:
        # print(context['form'])
        return render(request,'pages_main/cedric.html',context)