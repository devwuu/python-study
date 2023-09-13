from django.contrib import admin
from blog.models import Post, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'title',
        'author',
        'created_at',
        'updated_at'
    ]
    list_per_page = 10


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
