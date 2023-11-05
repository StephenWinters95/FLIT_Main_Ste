from django.contrib import admin
from datetime import datetime
from django_summernote.admin import SummernoteModelAdmin
from .models import Article
from .models import User
from .models import UserProfile
from .models import UserAction
from .models import UserFavourite


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_year', 'profile_image', 'created_on')
    search_fields = ['user']
    

@admin.register(UserAction)
class ActionAdmin(SummernoteModelAdmin):
    list_display = ('user', 'user_action_seq', 'parent_article', 'user_action_desc', 'user_action_taken', 
                    'observation', 'created_on', 'completed_on')
    list_filter = ('completed','user', 'user_action_seq', 'parent_article', 'created_on', )
    sortable_by = ['user', 'user_action_seq']
    search_fields = ['user', 'user_action_desc']

    actions = ['complete_actions']

    def complete_actions(self, request, queryset):
        queryset.update(completed=True, completed_on=datetime.now())
    
    
@admin.register(UserFavourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'favourite_article', 'created_on')
    list_filter = ('created_on', 'user', 'favourite_article')
    sortable_by = ['user', 'favourite_article']
    search_fields = ['user', 'favourite_article']
        