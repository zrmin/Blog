from django.contrib import admin

# 别忘了导入ArticlePost
from .models import ArticlePost

# 注册ArticlePost到admin种
admin.site.register(ArticlePost)
