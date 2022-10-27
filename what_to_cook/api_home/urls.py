from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    path('', views.login),   #api est nom de l'application definit sur views
    path('login/', views.page_home),
    path('api/', views.create_recipe),
    path('special/', views.special_view, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
]