# apps/blog/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# View mothod:posts
def posts(request):
	return render(request, 'blog/posts.html')


# View mothod:post
def post(request):
	return render(request, 'blog/post.html')