from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article
from fp_blog.models import Action

# Create your models here.
#User profile model extending allauth user model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    birth_year = models.PositiveIntegerField()
    age_approx = models.PositiveIntegerField()
    age_exact = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return f"User: {self.user.first_name} {self.user.last_name},  UserId: {self.user},  Email: {self.user.email},  Last login: {self.user.last_login.day}/{self.user.last_login.month}/{self.user.last_login.year}"

# Class UserAction, action that the user has copied from an article
class UserAction(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_actions" )
    user_action_seq = models.IntegerField(default=10)
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_personal_actions")
    user_action_desc = models.CharField(max_length=200, default='Action:  ')
    user_action_taken = models.CharField(max_length=200, default='Taken:  ')
    observation = models.CharField(max_length=200, default='Notes:  ')
    completed = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['user', 'user_action_seq']

    def __str__(self):
        return f"Action {self.user_action_seq} {self.user_action_desc} "

# Class UserFavourite, a set of Favourite Articles for the user
class UserFavourite(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favourite" )
    favourite_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_favourite")
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['user', 'created_on']

    def __str__(self):
        return f"User {self.user} {self.favourite_article} "
