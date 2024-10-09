from .models import Comment, Article, User, Action
from fp_personal.models import UserProfile
from django import forms
from .widgets import CustomClearableFileInput


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


# DMcC 09/10/24 - Copy through the ProductForm to ArticleForm
class ArticleForm(forms.ModelForm):
    # this class gives article visibility
    class Meta:
        model = Article
        # fields = ('title', 'slug', 'status', )
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # permit only the friendly names for the choices in product category
        # self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'




class ActionForm(forms.ModelForm):
    # this class provides for actions/tasks that are associated with articles
    class Meta:
        model = Action
        fields = ('article', 'action_desc',)
