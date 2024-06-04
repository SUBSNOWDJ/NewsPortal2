from django.contrib import admin
from .models import User, Author, Category, Post, PostCategory, Comment, News

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(News)

# Register your models here.