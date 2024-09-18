from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import User
from .models import Article
from .models import Action
from .models import Comment


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    # The Article is the main engine of the blog.  It uses Summernote to
    # control content editing.
    summernote_fields = ('content')

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'updated_on')
    list_display = ('title', 'slug', 'status', 'updated_on', 'created_on')
    search_fields = ['title', 'content']
    actions = ['approve_draft']

    def approve_draft(self, request, queryset):
        # this function allows an article to progress from draft to published
        queryset.update(status='1')


@admin.register(Action)
class ActionAdmin(SummernoteModelAdmin):
    # An article may have 0 or many actions (tasks) associated with it.
    # These action tasks act as a template for user tasks which are
    # later created within the fp_personal app
    list_filter = ('article', 'action_seq', 'created_on')
    list_display = ('article','action_seq', 'action_desc')
    raw_id_fields=['article']
    sortable_by = ['article', 'action_seq']
    search_fields = ['article', 'action_desc']
    ordering = ['article', 'action_seq']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # An article may have 0 to many comments assoiated with it.  A comment
    # always has a parent article
    list_display = ('user', 'body', 'article', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_field = ('user', 'article', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # this function allows unapproved comments to be moderated
        queryset.update(approved=True)
