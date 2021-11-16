# apps/home/urls.py

# Django modules
from django.urls import path

# Locals
from apps.home import views  

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
