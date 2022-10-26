from django.shortcuts import render
from .forms import MyForm

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

def create_recipe(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(dict(form.data)['proteins'])
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form })