# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Home
    path('', include('apps.home.urls', namespace='home')),

    # Shop
    path('', include('apps.shop.urls', namespace='shop')),

    # Blog
    path('', include('apps.blog.urls', namespace='blog')),

    # About
    path('', include('apps.about.urls', namespace='about')),

    # Contact
    path('', include('apps.contact.urls', namespace='contact')),

    # Account
    path('', include('apps.account.urls', namespace='account')),

    # Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)