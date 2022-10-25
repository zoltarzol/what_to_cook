from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    path('', views.login),   #api est nom de l'application definit sur views
    path('login/', views.page_home),
    path('api/', views.index, name = 'page_api'),

]