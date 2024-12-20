from django.contrib import admin
from datetime import datetime
from .models import User
from .models import Course, CourseContent, Cohort, Quiz , Progress

# Register your models here.
# The UserProfile model is a custom extension of allauth User model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'version', 'disp_seq', 'title', 'status',)
    search_fields = ['title']

@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'version', 'seq_num', 'article',)
    search_fields = ['article']

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display=('cohort_code', 'title', 'subtitle', 'status')
    search_fields=['cohort_code']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display=('quiz_code', 'question_text')    
    search_fields=['quiz_code']
    
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display=('user', 'course' , 'sequence_number' , 'completed')    
    search_fields=['user','course']
    