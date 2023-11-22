from django.contrib import admin
from datetime import datetime
from django_summernote.admin import SummernoteModelAdmin
from .models import Article
from .models import User
from .models import UserProfile, UserAction, Feedback


# The UserProfile model is a custom extension of allauth User model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_year', 'profile_image', 'created_on')
    search_fields = ['user']


# UserAction is a task instance that is applied to a user
# and includes follow-up tracking fields
@admin.register(UserAction)
class ActionAdmin(SummernoteModelAdmin):
    list_display = ('user', 'user_action_seq', 'parent_article',
                    'user_action_desc', 'user_action_url', 'user_action_taken',
                    'observation', 'created_on', 'completed_on')
    list_filter = ('completed', 'user', 'user_action_seq', 'parent_article',
                   'created_on', )
    sortable_by = ['user', 'user_action_seq']
    search_fields = ['user', 'user_action_desc']

    actions = ['complete_actions']

    def complete_actions(self, request, queryset):
        """ complete_actions is used to complete a user action """
        queryset.update(completed=True, completed_on=datetime.now())
