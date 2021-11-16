# apps/shop/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# View mothod:products
def products(request):
	return render(request, 'shop/products.html')
	

# View mothod:product
def product(request):
	return render(request, 'shop/product.html')