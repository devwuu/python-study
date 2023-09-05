from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

# CBV (Class Based View)
class PostList(ListView):
    model = Post
    template_name = 'list.html'
    ordering = '-created_at'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
