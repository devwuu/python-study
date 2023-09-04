from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 월 일 시 분 초
    updated_at = models.DateTimeField(auto_now=True)  # 월 일 시 분 초

    def __str__(self):
        return f'[{self.pk}] {self.title}'
