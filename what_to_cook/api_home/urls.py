from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    path('login/', views.login),   #api est nom de l'application definit sur views
    path('register/', views.register),
    path('home/', views.page_home),
    path('api/', views.ingred_fnct, name = 'page_api'),

]