from . import views
from django.urls import path

# paths within the fp_courses app
urlpatterns = [
    path('user-cohorts-courses/', views.user_cohorts_courses, name='user_cohorts_courses'),   #added DMcC 26/11/24
    ]

# Error handlers for site errors
handler404 = 'fp_blog.views.error_404'
handler500 = 'fp_blog.views.error_500'
handler403 = 'fp_blog.views.error_403'
handler400 = 'fp_blog.views.error_400'
