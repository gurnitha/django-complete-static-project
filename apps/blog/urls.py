# apps/blog/urls.py

# Django modules
from django.urls import path

# Locals
from apps.blog import views  

app_name = 'blog'

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/1', views.post, name='post'),
]
