from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.

# CBV (Class Based View)
class PostList(ListView):
    model = Post
    template_name = 'list.html'
    ordering = '-created_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categorys'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'

