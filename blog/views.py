from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.

# CBV (Class Based View)
class PostList(ListView):
    model = Post
    template_name = 'list.html'
    ordering = '-created_at'
