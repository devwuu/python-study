from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.

# CBV (Class Based View)
class PostList(ListView):
    model = Post
    # ListView를 상속 받았기 때문에 .all()을 자동으로 실행해준다.
    template_name = 'list.html'
    ordering = '-created_at'

    # 추가적으로 필요한 데이터를 가져오기 위해 오버라이딩 함
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categorys'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post
    # DetailView를 상속 받았기 때문에 .get(pk=)를 자동으로 실행해준다.
    template_name = 'detail.html'
    # class name과 template name이 같으면 템플릿 네임 생략 가능

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categorys'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


# FBV(Function Base View)
def category_page(request, slug):

    # get()은 단일, filter는 복수개

    if slug == 'none':
        category=None
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
        # 변수 scope는 해당 함수 내부까지

    return render(
        request,
        'list.html',
        {
            'post_list': post_list,
            'categorys': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category
        }
    )
