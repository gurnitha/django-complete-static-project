# apps/account/urls.py

# Django modules
from django.urls import path

# Locals
from apps.account import views  

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]
