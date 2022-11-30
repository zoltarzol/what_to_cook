from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    path('', views.page_home, name ='home'),
    path('api/', views.create_recipe, name ='api'),
    #path('special/', views.create_recipe, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('recipe/', views.recipe_rslt),
]