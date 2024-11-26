# paths within the fp_courses app
urlpatterns = [
    path('', views.CourseList, name='home'),
    path('my_courses/', views.my_courses, name='my_courses'),   #added Ste 22/11/24
    ]

# Error handlers for site errors
handler404 = 'fp_blog.views.error_404'
handler500 = 'fp_blog.views.error_500'
handler403 = 'fp_blog.views.error_403'
handler400 = 'fp_blog.views.error_400'
