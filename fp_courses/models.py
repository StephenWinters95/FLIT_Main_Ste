from django.db import models
from datetime import timedelta, datetime, date
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fp_blog.models import Article, Comment, Action


STATUS = ((0, "Inactive"), (1, "Active"))
CONTENT_TYPE = ((0, "Article"), (1, "Quiz"))

def today_plus_one_year():
    return date.today() + timedelta(days=365)

def today_plus_10_years():
    return date.today() + timedelta(days=3650)

def today_date():
    return date.today()

# Create your models here.
class Course(models.Model):
    """ Course is a set of articles delivered in a particular sequence
    fields: course_code, title1, slug, title2, version, author, featured_image, effective_from, effective_to"""
    disp_seq = models.IntegerField(default=10)
    course_code = models.CharField(max_length = 15, primary_key = True)
    version = models.CharField(max_length = 3)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="courses", db_constraint=False)
    featured_image = CloudinaryField('image', default='placeholder')
    effective_from = models.DateField(auto_now_add=True)
    effective_to = models.DateField(default=today_plus_10_years)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        unique_together = (('course_code', 'version'),)
        
        """ returns an overall list """
        ordering = ['disp_seq', 'course_code', 'version']

    def __str__(self):
        """ returns course code """
        print (self.course_code)
        return self.course_code 

    def is_valid_today(self):
        """ returns True or False based on effectivedate and status """
        valid_today = (( date.today >= self.effective_from) and (date.today <= date.effective_to) and (self.status))
        return (valid_today)

class CourseContent(models.Model):
    """ Course is a set of articles delivered in a particular sequence
    fields: course_code, title1, slug, title2, version, author, featured_image, effective_from, effective_to"""
    # Note that each line of course content has unique course_code/version/seq# combination
    # Every record refers to either a particular article or a particular quiz
    # Because foreign keys dont allow blanks, there will be one dummy article and one dummy quiz as placeholders
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="course_contents", db_constraint=False)
    version = models.CharField(max_length = 3)
    seq_num = models.IntegerField(default=10)
    content_type = models.IntegerField(choices=CONTENT_TYPE, default=0) 
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="course_article", db_constraint=False)
    # DMcC 20/12/24 Add in quiz as a foreign key within a particular course content
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name="course_quiz", db_constraint=False, null=True)
    status = models.IntegerField(choices=STATUS, default=0)    
    
    class Meta:
        unique_together = ('course_code', 'version', 'seq_num')
        
        """ returns an overall list """
        ordering = ['course_code', 'version', 'seq_num']

    def __str__(self):
        """ returns course title """
        return f"{self.course_code} {self.version} {self.seq_num}" 
    

    def is_valid(self):
        """ Returns True or False based on CourseContent status """
        valid_today = (self.status)
        return (valid_today)


class Cohort(models.Model):
    """ Cohort refers to a group of users who will be assigned to a common course of learning """
    cohort_code = models.CharField(max_length = 25, primary_key = True)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="admin_cohorts", db_constraint=False)
    featured_image = CloudinaryField('image', default='placeholder')
    effective_from = models.DateField(auto_now_add=True)
    effective_to = models.DateField(default=today_plus_one_year)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    members = models.ManyToManyField(User, related_name='cohort_user', blank=True)
    courses = models.ManyToManyField(Course, related_name='cohort_course', blank=True)
    
    class Meta:
        """ returns an overall list """
        ordering = ['cohort_code']

    def __str__(self):
        """ returns course title """
        return f"{self.cohort_code}: {self.title}"
    
    def is_valid_today(self):
        """ returns True or False based on effectivedate and status """
        valid_today = (( date.today >= self.effective_from) and (date.today <= date.effective_to) and (self.status))
        return (valid_today)
    

class Quiz(models.Model):
    """ Quiz is a multichoice set of questions related to a particle topic or article
        fields: course_code, title1, slug, title2, version, author, featured_image, effective_from, effective_to"""
    quiz_code = models.CharField(max_length=25, primary_key = True)
    question_text = models.CharField(max_length = 200, default='Question text goes here?')
    ans1_text = models.CharField(max_length=200, default="Answer1 goes here")
    ans2_text = models.CharField(max_length=200, default="Answer2 goes here")
    ans3_text = models.CharField(max_length=200, default="Answer3 goes here")
    ans4_text = models.CharField(max_length=200, default="Answer4 goes here")
    correct_ans = models.IntegerField()
    explanation = models.CharField(max_length=300, default="Correct answer is X:  This is because ......")
    status = models.IntegerField(choices=STATUS, default=0)    
    
    class Meta:
        """ returns an overall list """
        ordering = ['quiz_code',]

    def __str__(self):
        """ returns quiz question """
        return f"{self.quiz_code} {self.question_text}" 

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    version = models.CharField(max_length=50) 
    sequence_number = models.IntegerField()  # Field for sequence number
    score = models.FloatField()  # or IntegerField, depending on your needs
    completed = models.BooleanField(default=False)  # Boolean to track completion status
    date_completed = models.DateTimeField(null=True, blank=True)  # Date completed field
    

    class Meta:
        unique_together = ('user', 'course')  # This ensures a user can only have one progress entry per course

    def __str__(self):
        return f"{self.user.username} - {self.course.name} (v{self.course.version}): {self.score}, Completed: {self.completed}"