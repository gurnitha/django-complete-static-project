# apps/about/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# View mothod:about
def about(request):
	return render(request, 'about/about.html')
