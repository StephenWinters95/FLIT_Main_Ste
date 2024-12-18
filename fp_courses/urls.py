from . import views
from django.urls import path

# paths within the fp_courses app
urlpatterns = [
    path('user_cohorts_courses/', views.user_cohorts_courses, name='user_cohorts_courses'),   #added DMcC 26/11/24
    path('maint_quizzes/', views.maint_quizzes, name='maint_quizzes'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('edit_quiz/<int:id>/', views.edit_quiz, name='edit_quiz'),
    path('delete_quiz/<int:id>/', views.delete_quiz, name='delete_quiz'),
    path('quiz_preview/<int:quiz_code>/', views.quiz_preview, name='quiz_preview'),
    path('maint_courses/', views.maint_courses, name='maint_courses'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
    path('course_preview/<int:course_code>/', views.course_preview, name='course_preview'),
    ]

# Error handlers for site errors
handler404 = 'fp_blog.views.error_404'
handler500 = 'fp_blog.views.error_500'
handler403 = 'fp_blog.views.error_403'
handler400 = 'fp_blog.views.error_400'
