from django.contrib import admin

from myblog.models import Post
from myblog.models import Category

class CategoryAdmin(admin.ModelAdmin):
    # this affects the add category form, not the first list of all categories
    fields = ('name', 'description')

class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    # this affects the add post form, not the list of posts
    fields = ('title','text', 'author', 'categories')
    # fields = ('title','text', 'author', 'categories') I tried this
    inlines = [
        CategoryInline,
    ]

admin.site.register(Category, CategoryAdmin)   
admin.site.register(Post, PostAdmin)
