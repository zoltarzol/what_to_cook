from django.urls import path
from . import views


#api est nom de l'application definit sur views
app_name = "user_app"

urlpatterns = [
 path('login/', views.login),   
 path('register/', views.register),
]