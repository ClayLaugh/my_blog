from django.contrib import admin
from .models import ArticlePost

# 注册ArticlePost到Admin中
admin.site.register(ArticlePost)
