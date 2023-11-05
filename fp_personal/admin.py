from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin
from .models import User
from .models import UserProfile
from .models import UserAction

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'birth_year', 'last_login')
    search_fields = ['user', 'email']
    

@admin.register(UserAction)
class ActionAdmin(SummernoteModelAdmin):
    list_display = ('user', 'user_action_seq', 'parent_article', 'action_desc', 'action_taken', 
                    'observation', 'created_on', 'completed_on')
    list_filter = ('user', 'user_action_seq', 'parent_article', 'created_on', 'completed')
    sortable_by = ['user', 'user_action_seq']
    search_fields = ['user', 'action_desc']

    actions = ['complete_actions']

    def complete_actions(self, request, queryset):
        queryset.update(completed=True)