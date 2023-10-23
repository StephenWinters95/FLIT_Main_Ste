from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

# This line replaced with @admin.register(Article)
# admin.site.register(Article)
# @admin.register(Article) registers both the artice model and the ArticleAdmin class

