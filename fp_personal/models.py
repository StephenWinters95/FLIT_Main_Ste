from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article, Comment, Action


# Create your models here.
# User profile model extending allauth user model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    birth_year = models.PositiveIntegerField()
    age_approx = models.PositiveIntegerField()
    age_exact = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def number_of_likes(self):
        return self.user.article_like.count()
  
    def bookmarks(self):
        return self.user.article_favourite.article

    def number_of_bookmarks(self):
        return self.user.article_favourite.count()

    def comments(self):
        return (self.user.user_comments)

    def number_of_comments(self):
        return self.user.user_comments.count()

    def number_of_valid_comments(self):
        return (self.user.user_comments.filter(approved=True).count())

    def actions(self):
        return (self.user.user_actions)

    def number_of_actions(self):
        return (self.user.user_actions.count())

    def number_of_completed_actions(self):
        return (self.user.user_actions.filter(completed=True).count())

    def number_of_incomplete_actions(self):
        return (self.user.user_actions.filter(completed=False).count())

    def __str__(self):
        return f"UserName: {self.user.first_name} {self.user.last_name},"
        + f" User: {self.user}, Email: {self.user.email},"
        + f" Last login: {self.user.last_login.day}/"
        + f"{self.user.last_login.month}/{self.user.last_login.year}"


# Class UserAction, action that the user has copied from an article
class UserAction(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_actions" )
    user_action_seq = models.IntegerField(default=10)
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE, 
                                       related_name="parent_article")
    user_action_desc = models.ForeignKey(Action, on_delete=models.CASCADE, 
                                         related_name="parent_action")
    user_action_url = models.URLField(blank=True)
    user_action_taken = models.CharField(max_length=200, default='Done so far:  ')
    observation = models.CharField(max_length=200, default='Results:  ')
    completed = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['user', 'user_action_seq', 'created_on']

    def my_actions(request):
        my_actions = UserAction.objects.filter(user=request.user.id).order_by('user_action_seq', 'created_on')
        return my_actions
   
    def __str__(self):
        return f"{self.user} {self.user_action_seq} {self.user_action_desc}"
        +f" {self.completed} {self.completed_on} "

STATUS = ((0, "Draft"), (1, "Published"))
FTYPE = (("F", "Feedback"), ("T", "Testimonial"))


class Feedback(models.Model):
    person = models.CharField(max_length=30, default="Console")
    email = models.EmailField(default="your_email@gmail.com")
    type = models.TextField(max_length=1, default="F") 
    created_on = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(max_length=500, blank=True)
    followup = models.TextField(max_length=500, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    completed = models.BooleanField(null=False, blank=False)
    completed_on = models.DateTimeField(blank=True, null=True)
   

    class Meta:
        ordering = ['person', '-created_on']

    def __str__(self):
        return f"User: {self.person}, Email: {self.email},"
        + f"Created: {self.created_on} Completed: {self.completed}"
