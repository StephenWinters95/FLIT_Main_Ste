from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article, Comment, Action


# User profile model extending allauth user model
class UserProfile(models.Model):
    """ UserProfile class extends allauth User models
    includes profile_image and some age-related fields """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    birth_year = models.PositiveIntegerField()
    age_approx = models.PositiveIntegerField()
    age_exact = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ set ordering of user profiles to most recent first """
        ordering = ['-created_on']

    def number_of_likes(self):
        """ count of articles this user has liked """
        return self.user.article_like.count()

    def bookmarks(self):
        """ list of bookmarks/Reading List Items for a user """
        return self.user.article_favourite.article

    def number_of_bookmarks(self):
        """ count of bookmarks/Reading List Items for a user """
        return self.user.article_favourite.count()

    def comments(self):
        """ list of comments/'Responses' created by a user """
        return (self.user.user_comments)

    def number_of_comments(self):
        """ count of comments/'Responses' created by a user """
        return self.user.user_comments.count()

    def number_of_valid_comments(self):
        """ count of valid comments/'Responses' created by a user """
        return (self.user.user_comments.filter(approved=True).count())

    def actions(self):
        """ list of actions/'Tasks' created by a user """
        return (self.user.user_actions)

    def number_of_actions(self):
        """ count of actions/'Tasks' created by a user """
        return (self.user.user_actions.count())

    def number_of_completed_actions(self):
        """ count of actions/'Tasks' created by a user, marked completed """
        return (self.user.user_actions.filter(completed=True).count())

    def number_of_incomplete_actions(self):
        """ count of actions/'Tasks' created by a user, marked incomplete """
        return (self.user.user_actions.filter(completed=False).count())

    def __str__(self):
        """ returns user details from User and UserProfile joined """
        return f"UserName: {self.user.first_name} {self.user.last_name},"
        + f" User: {self.user}, Email: {self.user.email},"
        + f" Last login: {self.user.last_login.day}/"
        + f"{self.user.last_login.month}/{self.user.last_login.year}"


# Class UserAction, action that the user has created - by copying from article
# or creating independently from their 'My Tasks' - 'Create new Task'.
# It includes user and parent article/action & progress-tracking fields
class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_actions")
    user_action_seq = models.IntegerField(default=10)
    parent_article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                       related_name="parent_article")
    user_action_desc = models.ForeignKey(Action, on_delete=models.CASCADE,
                                         related_name="parent_action")
    user_action_url = models.URLField(blank=True)
    user_action_taken = models.CharField(max_length=200,
                                         default='Done so far:  ')
    observation = models.CharField(max_length=200, default='Results:  ')
    completed = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        """ returns sorted on seqence then creation-date as tie-breaker """
        ordering = ['user', 'user_action_seq', 'created_on']

    def my_actions(request):
        """ returns list of actions for a given user """
        my_actions_unord = UserAction.objects.filter(user=request.user.id)
        my_actions = my_actions_unord.order_by('user_action_seq', 'created_on')
        return my_actions

    def __str__(self):
        """ returns key user action fields from a user task perspective """
        return f"{self.user} {self.user_action_seq} {self.user_action_desc}"
        +f" {self.completed} {self.completed_on} "


STATUS = ((0, "Draft"), (1, "Published"))
FTYPE = (("F", "Feedback"), ("T", "Testimonial"))


# The feedback class is intended for site feedback.
# Not implemented at FinancialPlanner v1
# (Article response may achieve the same functional goal)
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
