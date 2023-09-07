from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    thumbnail = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                                  blank=True)  # MEDIA_ROOT의 하위 폴더로 'blog/images/%Y/%m/%d/' 디렉토리를 생성하고 파일을 저장한다
    file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    hook_text = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    # blank : 빈 값으로 저장 수정 허용
    # null : null 허용

    created_at = models.DateTimeField(auto_now_add=True)  # 월 일 시 분 초
    updated_at = models.DateTimeField(auto_now=True)  # 월 일 시 분 초

    # toString
    def __str__(self):
        return f'[{self.pk}] {self.title} || {self.author}'

    def get_file_name(self):
        return os.path.basename(self.file.name)


