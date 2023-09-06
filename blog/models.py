from django.db import models
import os


# Create your models here.
class Post(models.Model):
    thumbnail = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) # MEDIA_ROOT의 하위 폴더로 'blog/images/%Y/%m/%d/' 디렉토리를 생성하고 파일을 저장한다
    file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 월 일 시 분 초
    updated_at = models.DateTimeField(auto_now=True)  # 월 일 시 분 초

    # toString
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_file_name(self):
        return os.path.basename(self.file.name)
