from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    path('login/', views.login),   #api est nom de l'application definit sur views
    path('register/', views.register),
    path('', views.page_home),
    path('api/', views.create_recipe, name = 'page_api'),

]