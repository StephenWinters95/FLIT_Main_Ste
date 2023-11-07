from django import forms
from django.db import models
from .models import UserProfile, UserFavourite, UserAction



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'profile_image')

class UserFavouriteForm(forms.ModelForm):
    class Meta:
        model = UserFavourite
        fields = ('user', 'favourite_article')

class UserActionForm(forms.ModelForm):
    class Meta:
        model=UserAction
        fields=('user', 'user_action_seq', 'parent_article', 'user_action_desc', 'user_action_taken', 'observation', 'completed')
