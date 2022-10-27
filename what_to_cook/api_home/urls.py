from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    
    path ('', views.base),
    path('asking/', views.aask),
    path('recipe/', views.recipe_rslt),
]

