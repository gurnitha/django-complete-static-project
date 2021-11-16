# apps/account/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# View mothod:login
def login(request):
	return render(request, 'account/login.html')


# View mothod:profile
def profile(request):
	return render(request, 'account/profile.html')