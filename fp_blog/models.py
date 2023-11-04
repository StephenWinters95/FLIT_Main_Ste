from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="article_posts")
    content = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='article_like',
                                   blank=True)
    favourites = models.ManyToManyField(User, related_name='article_favourite',
                                        blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_comments(self):
        return self.body.count()


class Action(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="actions")
    action_seq = models.IntegerField(default=10)
    action_desc = models.CharField(max_length=200, default='Action:  ')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="action_created_by")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['article', 'action_seq']

    def __str__(self):
        return f"Action {self.action_seq} {self.action_desc} "


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
    parent_article = models.ManyToManyField(Article, related_name="article_personal_actions")
    action_desc = models.CharField(max_length=200, default='Action:  ')
    action_taken = models.CharField(max_length=200, default='Taken:  ')
    observation = models.CharField(max_length=200, default='Notes:  ')
    completed = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user_action_seq']

    def __str__(self):
        return f"Action {self.action_seq} {self.action_desc} "

