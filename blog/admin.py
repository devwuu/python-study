from django.contrib import admin
from blog.models import Post
from blog.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'title',
        'author',
        'created_at',
        'updated_at'
    ]
    list_per_page = 10


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
