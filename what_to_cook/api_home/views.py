from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'pages_main/login.html')




def page_home(request):
    return render(request, 'pages_main/home.html')
