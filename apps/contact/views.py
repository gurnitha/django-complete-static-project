# apps/contact/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# View mothod:contact
def contact(request):
	return render(request, 'contact/contact.html')
