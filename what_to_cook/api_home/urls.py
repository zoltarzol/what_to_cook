from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "api_home"

urlpatterns = [
    
    path ('', views.base),
    path('asking/', views.aask),
    path('recipe/', views.recipe_rslt),
    
]
urlpatterns += staticfiles_urlpatterns()

