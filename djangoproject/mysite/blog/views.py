from django.shortcuts import render
from .models import Post

def post_list(request):
    # Add an indented block here
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
