from .models import Comment, Article, User, Action, Survey
from fp_personal.models import UserProfile
from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

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
        fields = '__all__'
        widgets = {
            'bar': SummernoteInplaceWidget(),
        }

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

#added 16/10/24

class UserForm(forms.ModelForm):
    # Ste 16/10/24 8this class gives article visibility
    class Meta:
        model = User  # Assuming 'User' is your user model
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'password']   # You can specify specific fields if needed
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border-black rounded-0'}),
            'email': forms.EmailInput(attrs={'class': 'border-black rounded-0'}),
            # Add other fields as necessary
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


#Surveyform - 23/10/24 - Ste

class surveyForm(forms.ModelForm):
    class Meta:
        model =  Survey
        fields = '__all__'  
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'