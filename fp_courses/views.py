from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator  # Specifically imported 
from django.db.models import Q  # This is a text search capability
from .models import Course, Cohort, CourseContent, Quiz
from fp_personal.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
import pandas as pd
import numpy as np




# Create your views here.
def MyCourses(request):
    # courses need to link to articles and have a questionaire after them. possibly multiple questions.
    # so maybe is we had a 2d array where each column had the article and then multiple choice questions after them. 
    # courses Structure => courses[ Course ID, Course ID, Course ID,]    Main = [ID , Article ID , Quiz ID , Quiz ID , Quiz ID , Quiz ID]     Quiz[] =[Quiz ID , Q1 , ANS1 , ANS2 , ANS3 , ANS4 ,]  x several times etc. and that will be the course ANS1 will always be correct answer but the html will be told to randomize the order. 
    # List of Article ID's 
    # need to make a diffrent array for users scores and add it to their profile.
    # need to make a menu to display all courses.
    # need to make a page to allow an admin to make a custome test / course.
    
    # DMcC 26/11/24 - I need to do some more work to ensure only cohorts that are valid for the user are returned.... 
    # Just need to wait for my brain to become usable again!
    print("in view MyCourses, current user is ", request.user)
    cohorts = ['Public',]
    print("Initial cohorts (whether logged in or not) are ", cohorts)
    queryset1 = Cohort.objects.filter(status=1).order_by('-updated_on') 
    print("Additional cohorts for logged in user (not yet filtered by user) are", queryset1)
    courses = []
    queryset = Course.objects.filter(status=1).order_by('-updated_on')
    print(queryset)
    context = {
        queryset,
    }    
    return render(request, 'fp_courses/my_courses.html', context)

@login_required
def user_cohorts_courses(request):
  user = request.user
  
  # Get user's cohorts (adjust queryset based on your relationships)
  cohorts = user.cohort_user.all()

  # Iterate through cohorts and get assigned courses (adjust queryset)
  courses = []
  for cohort in cohorts:
    assigned_courses = cohort.course.all()
    courses.extend(assigned_courses)

  context = {
      'cohorts': cohorts,
      'courses': courses,
  }
  return render(request, 'user_cohorts_courses.html', context)