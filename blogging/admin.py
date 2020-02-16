from django.contrib import admin
from django import forms
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        ]
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
