from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='my_planner'),
    path('copy_action/<int:pk>', views.copyUserAction, name='copy_action'),
    path('create_action/', views.createUserAction, name='create_action'),
    path('update_action/<int:pk>/', views.updateUserAction, name='update_action'),
    path('delete_action/<int:pk>/', views.deleteUserAction, name='delete_action'),
    path('delete_bookmark/<int:pk>/', views.deleteBookmark, name='delete_bookmark'),
    path('delete_comment/<int:pk>/', views.deleteComment, name='delete_comment'),

    
]
