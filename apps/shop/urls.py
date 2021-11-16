# apps/shop/urls.py

# Django modules
from django.urls import path

# Locals
from apps.shop import views  

app_name = 'shop'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/1/', views.product, name='product'),
]
