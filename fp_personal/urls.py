from . import views
from django.urls import path

# URL paths for fp_personal app
urlpatterns = [
    path(' ', views.UserProfileView.as_view(), name='my_planner'),
    path('create_action/', views.createUserAction, name='create_action'),
    path('copy_action/<int:pk>', views.copyUserAction, name='copy_action'),
    path('update_action/<int:pk>/', views.updateUserAction,
         name='update_action'),
    path('delete_action/<int:pk>/', views.deleteUserAction,
         name='delete_action'),
    path('delete_bookmark/<int:pk>/', views.deleteBookmark,
         name='delete_bookmark'),
    path('delete_comment/<int:pk>/', views.deleteComment,
         name='delete_comment'),
    path('create_user/', views.addUserProfile, name='create_user'),
    path('update_user/<int:pk>/', views.updateUserProfile, name='update_user'),
    path('about/', views.FeedbackList.as_view(), name='about'),
]


# Error handling
handler404 = 'fp_personal.views.error_404'
handler500 = 'fp_personal.views.error_500'
handler403 = 'fp_personal.views.error_403'
handler400 = 'fp_personal.views.error_400'
