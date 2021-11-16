# apps/about/urls.py

# Django modules
from django.urls import path

# Locals
from apps.about import views  

app_name = 'about'

urlpatterns = [
    path('about/', views.about, name='about'),
]
