from django.shortcuts import redirect, render

from django.views.generic import *
from .models import Students
from .forms import StudentsForm, test




# Create your views here.

def login(request):
    return render(request,'pages_main/login.html')




def page_home(request):
    return render(request, 'pages_main/home.html')



#formulaire soit visible

def index(request):
    if request.method == "POST":
        form = StudentsForm(request.POST).save()
        return redirect('/api')
    else :
        form = StudentsForm()

    return render(request, 'pages_main/api_page.html', {'form' : form})


def nour(request):

    form = test()

    return render(request, 'pages_main/api_page.html', {'form' : form})

