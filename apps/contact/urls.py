# apps/contact/urls.py

# Django modules
from django.urls import path

# Locals
from apps.contact import views  

app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
