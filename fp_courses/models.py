from django.db import models
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article, Comment, Action

STATUS = ((0, "Inactive"), (1, "Active"))
CONTENT_TYPE = ((0, "Article"), (1, "Quiz"))

# Create your models here.
class Course(models.Model):
    """ Course is a set of articles delivered in a particular sequence
    fields: course_code, title1, slug, title2, version, author, featured_image, effective_from, effective_to"""
    disp_seq = models.IntegerField(default=10)
    course_code = models.CharField(max_length = 15, primary_key = True)
    version = models.CharField(max_length = 3)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="courses", db_constraint=False)
    featured_image = CloudinaryField('image', default='placeholder')
    effective_from = models.DateTimeField(auto_now_add=True)
    effective_to = models.DateTimeField(default=datetime.today() + timedelta(days=3652))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        unique_together = (('course_code', 'version'),)
        
        """ returns an overall list """
        ordering = ['disp_seq', 'course_code', 'version']

    def __str__(self):
        """ returns course code """
        print (self.course_code)
        return self.course_code 

class CourseContent(models.Model):
    """ Course is a set of articles delivered in a particular sequence
    fields: course_code, title1, slug, title2, version, author, featured_image, effective_from, effective_to"""
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="course_contents", db_constraint=False)
    version = models.CharField(max_length = 3)
    seq_num = models.IntegerField(default=10)
    content_type = models.IntegerField(choices=CONTENT_TYPE, default=0) 
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="course_article", db_constraint=False)
    status = models.IntegerField(choices=STATUS, default=0)    
    
    class Meta:
        unique_together = ('course_code', 'version', 'seq_num')
        
        """ returns an overall list """
        ordering = ['course_code', 'version', 'seq_num']

    def __str__(self):
        """ returns course title """
        return f"{self.course_code} {self.version} {self.seq_num}" 
    

class Cohort(models.Model):
    """ Cohort refers to a group of users who will be assigned to a common course of learning """
    cohort_code = models.CharField(max_length = 25, primary_key = True)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="admin_cohorts", db_constraint=False)
    featured_image = CloudinaryField('image', default='placeholder')
    effective_from = models.DateTimeField(auto_now_add=True)
    effective_to = models.DateTimeField(default=datetime.today() + timedelta(days=365))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        """ returns an overall list """
        ordering = ['cohort_code']

    def __str__(self):
        """ returns course title """
        return f"{self.cohort_code}: {self.title}"


class CohortUser(models.Model):
    cohort_code = models.ForeignKey(Cohort, on_delete=models.CASCADE,
                                     related_name="cohort_users" )
    user=models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="learner_cohorts", db_constraint=False)

    class Meta:
        unique_together = ('cohort_code', 'user') 
        """ returns an overall list """
        ordering = ['cohort_code', 'user']

    def __str__(self):
        """ returns course title """
        return f"{self.cohort_code} {self.user}"
