from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify


# 현재 쿼리 최적화를 하지 않고 자동 발생하는 쿼리에 의존해서 데이터를 가져오다보니
# 관계가 있는 모델의 경우 아이디별로 쿼리가 발생하는 현상이 발생
# 실무에서 사용하기 위해선 최적화가 필요할 것 같다

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


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    # 로그인한 유저에게만 해당 페이지가 보여지게 된다
    # form이라는 이름의 table 형태로 form을 제공한다
    template_name = 'create-form.html'
    model = Post
    fields = ['title', 'content', 'hook_text', 'thumbnail', 'file', 'category']

    # 최고 관리자거나 관리자가 아니면 현재 페이지에 접근할 수 없다
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    # 사용자가 form에 제대로 된 정보를 담으면 실행되는 함수
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):

            form.instance.author = current_user
            post = super(PostCreate, self).form_valid(form)  # 이 시점에서 새로운 Post가 DB에 저장된다. self.object도 이때 만들어진다.

            if self.request.POST.get('tags_str'):
                tag_list = self.request.POST.get('tags_str').__str__().split(';')
                for tag in tag_list:
                    slug = slugify(tag.strip(), allow_unicode=True)
                    saved_tag, is_created = Tag.objects.get_or_create(name=tag, slug=slug)  # 신규 tag가 있다면 Tag를 저장해주는 작업
                    self.object.tags.add(saved_tag)  # 이미 저장되어 있던 Post에 Tag를 추가해서 저장해주는 작업
                    # 여기서 self.objects가 가능한 이유는 상단에서 이미 post를 저장했기 때문이다.

            return post
        else:
            redirect('/blog/')


class PostUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'update-form.html'
    model = Post
    fields = ['title', 'content', 'hook_text', 'thumbnail', 'file', 'category', 'tags']  # 이렇게 tags를 추가해도 됨

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            # self.get_object()는 Post.objects.get(pk=pk)와 동일하다. 현재 View에서 보여주는 Object를 가져오는 것이기 때문에
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# FBV(Function Base View)
def category_page(request, slug):
    # get()은 단일, filter는 복수개

    if slug == 'none':
        category = None
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


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)

    return render(
        request,
        'list.html',
        {
            'post_list': tag.post_set.all(),  # Post.objects.filter(tags=tag),
            'categorys': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )
