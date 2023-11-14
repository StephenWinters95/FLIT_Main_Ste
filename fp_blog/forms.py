from .models import Comment, Article, User, Action
from fp_personal.models import UserProfile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'article', 'body', 'approved')

    
class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('article', 'action_desc')

#class UserBookmarkForm(forms.ModelForm):
#    class Meta:
#        model = Article
#        fields = ('user', 'article_favourite')
