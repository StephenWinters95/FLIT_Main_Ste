from django import forms
from django.db import models
from .models import UserProfile, UserAction
from fp_blog.models import Article, Action, Comment
# from .models import UserProfile, UserFavourite, UserAction


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'profile_image', 'birth_year', 'age_approx',
                  'age_exact', )
# DMcC 18/11/23 hide user on html form display rather than on extract:
#        exclude = ['user',]

    birth_year = models.PositiveIntegerField()
    age_approx = models.PositiveIntegerField()
    age_exact = models.PositiveIntegerField()
    profile_image = "../../static/images/placeholder.png"


class UserActionForm(forms.ModelForm):
    class Meta:
        model = UserAction
        fields = ('user', 'user_action_seq', 'parent_article',
                  'user_action_desc', 'user_action_url', 'user_action_taken',
                  'observation', 'completed', 'completed_on',)
