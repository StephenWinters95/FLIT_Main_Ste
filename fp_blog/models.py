from django.db import models
from datetime import date
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # needed for images
from taggit.managers import TaggableManager  # needed for Article tags
from django.core.validators import MinValueValidator, MaxValueValidator # added 01/11/24

STATUS = ((0, "Draft"), (1, "Published"))
GENDER_CHOICES = (('M', "Male"), ("F", "Female"), ("N", "Non-binary"), ("O", "Other"), ("U", "Unanswered"))
# Marital status
MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
]
# Accomodation status
ACCOMMODATION_CHOICES = [
    ('homeless', 'Homeless'),
    ('renting', 'Renting'),
    ('living_with_family', 'Living with Family'),
    ('own_home_mortgage', 'Own my own home but paying mortgage'),
    ('own_home_no_mortgage', 'Own my own home and not paying mortgage'),
]
# Accomodation status
FIN_DEC_MAKING_CHOICES = [
    ('self', 'for me'),
    ('sepa', 'for me and my partner'),
    ('sefa', 'for me and my family'),
    ('seot', 'for me and other people outside my immediate family'),
]


# model Article is the 'engine' of this site, articles are designed
# to hold source information which is referenced in other models
# (including models within sibling apps)
class Article(models.Model):
    """Article is the core Model for FinancialPlanner site
    fields: title, slug, author, content, image_field, excerpt, date and tag"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="article_posts", db_constraint=False)
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
    tags = TaggableManager()  # external python utility for x-refs

    class Meta:
        """ returns an overall list """
        ordering = ['-created_on']

    def __str__(self):
        """ returns article title """
        return self.title

    def number_of_likes(self):
        """ returns count of user 'likes' for an article """
        return self.likes.count()

    def number_of_bookmarks(self):
        """ returns count of user 'bookmarks' for an article """
        return self.favourites.count()

    def number_of_comments(self):
        """ returns number of user Responses for this article """
        return self.comments.count()

    def number_of_valid_comments(self):
        """ returns number of approved/moderated user Responses for article """
        return (self.comments.filter(approved=True).count())


# Comment model is a secondary data structure, a comment, termed within the app
# as 'Response', is always associated with a particular article and user
class Comment(models.Model):
    """ Comment is a secondary data structure, a comment ('Response')
    is created against an article """
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments", db_constraint=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_comments", db_constraint=False)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # return comments sequenced from earliest to latest creation
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """ returns descriptor for a parameterised comment  """
        return f"Comment {self.body} by user {self.user}"

    def number_of_comments(self):
        """ returns number of comments """
        return self.body.count()


# class Action is a form of mass protest popularised in the US Court System
# Action model, by contrast, relates to a follow-on Task associated with an
# article.  An Action is initially associated with a parent Article, and
# includes a sequence#, a task description, and possibly an associated URL
class Action(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="actions", db_constraint=False)
    action_seq = models.IntegerField(default=10)
    action_desc = models.CharField(max_length=200, default='Action:  ')
    action_url = models.URLField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="action_created_by", db_constraint=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['article', 'action_seq']

    def __str__(self):
        return self.action_desc



# created 01/11/24 by ste
# made as a replacement for UserProfile Model 
# will allow a webiste user to fill out form without needing to be logged in
# form is unique and currently a better layout than userProfile.

class Survey(models.Model):
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        )
     
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(120)])
    income = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)]) # Consider using choices for radio boxes
    number_children = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(30)])
    income_type = models.CharField(max_length=100)
    main_income_source = models.CharField(max_length=100)
    other_income_sources = models.TextField(blank=True)
    
    marital_status = models.CharField(
        max_length=50,
        choices=MARITAL_STATUS_CHOICES,
        default='single',  # You can set a default value if you want
    )
    accommodation_status = models.CharField(
        max_length=50,
        choices=ACCOMMODATION_CHOICES,
        default='available',  # Set a default value if needed
    )
    ##
    accommodation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_adults_living_with = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(45)])
    financial_admin_for = models.CharField(max_length=100)
    life_stage = models.CharField(max_length=100)
    life_events = models.TextField(blank=True)
    welfare_schemes = models.CharField(max_length=100)
    


