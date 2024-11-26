from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator  # Specifically imported 
from django.db.models import Q  # This is a text search capability
from .models import Course, Cohort, CourseContent, Quiz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
import pandas as pd
import numpy as np




# Create your views here.
def my_courses(request):
    # courses need to link to articles and have a questionaire after them. possibly multiple questions.
    # so maybe is we had a 2d array where each column had the article and then multiple choice questions after them. 
    # courses Structure => courses[ Course ID, Course ID, Course ID,]    Main = [ID , Article ID , Quiz ID , Quiz ID , Quiz ID , Quiz ID]     Quiz[] =[Quiz ID , Q1 , ANS1 , ANS2 , ANS3 , ANS4 ,]  x several times etc. and that will be the course ANS1 will always be correct answer but the html will be told to randomize the order. 
    # List of Article ID's 
    # need to make a diffrent array for users scores and add it to their profile.
    # need to make a menu to display all courses.
    # need to make a page to allow an admin to make a custome test / course.
    
    courses = []
    queryset = Course.objects.filter(status=1).order_by('-updated_on')
    print(queryset)
    
    return render(request, 'fp_courses/my_courses.html')

