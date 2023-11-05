from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article
from fp_blog.models import Action

# Create your models here.
#User profile model extending allauth user model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')
    birth_year = models.PositiveIntegerField()
    age_approx = models.PositiveIntegerField()
    age_exact = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"Hi {self.name}"

# Class UserAction, action that the user has copied from an article
class UserAction(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_actions" )
    user_action_seq = models.IntegerField(default=10)
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_personal_actions")
    action_desc = models.CharField(max_length=200, default='Action:  ')
    action_taken = models.CharField(max_length=200, default='Taken:  ')
    observation = models.CharField(max_length=200, default='Notes:  ')
    completed = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user', 'user_action_seq']

    def __str__(self):
        return f"Action {self.action_seq} {self.action_desc} "
