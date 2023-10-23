from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin
from .models import Action
from .models import Comment

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    actions = ['approve_draft']

    def approve_draft(self, request, queryset):
        queryset.update(status='1')

# This line replaced with @admin.register(Article)
# admin.site.register(Article)
# @admin.register(Article) registers both the artice model and the 
# ArticleAdmin class


@admin.register(Action)
class ActionAdmin(SummernoteModelAdmin):
    
    list_filter = ('article', 'created_on')
    list_display = ('article', 'action_seq', 'action_desc', 'created_on')
    search_fields = ['article', 'action_desc']
