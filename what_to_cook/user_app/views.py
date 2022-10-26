from django.shortcuts import render
from django.views.generic import *


# Create your views here.

def login(request):
    return render(request,'pages_main2/login.html')



def register(request):
    return render(request,'pages_main2/register.html')

