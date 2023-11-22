from .models import Comment, Article, User, Action
from fp_personal.models import UserProfile
from django import forms


class CommentForm(forms.ModelForm):
    # this class provides a comment form for new comment creation
    class Meta:
        model = Comment
        fields = ('body', )


class UserCommentForm(forms.ModelForm):
    # this class provides visibility of comments created by a particular user
    class Meta:
        model = Comment
        fields = ('user', 'article', 'body', 'approved', )


class ArticleForm(forms.ModelForm):
    # this class gives article visibility
    class Meta:
        model = Article
        fields = ('title', 'slug', 'status', )


class ActionForm(forms.ModelForm):
    # this class provides for actions/tasks that are associated with articles
    class Meta:
        model = Action
        fields = ('article', 'action_desc',)
