from django.urls import path
from . import views


#api est nom de l'application definit sur views
app_name = "api_home"

urlpatterns = [
   
    path('home/', views.page_home, name = 'home'),
    path('api/', views.create_recipe, name = 'page_api'),
    path('special/', views.special_view, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),

]


#urlpatterns = [
 #path('login/', views.login),   
# path('register/', views.register),
# path('accounts/', include('django.contrib.auth.urls'))]

