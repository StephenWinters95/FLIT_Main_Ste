from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='my_planner'),
    path('create_action/', views.createUserAction, name='create_action'),
    path('update_action/<int:pk>/', views.updateUserAction, name='update_action'),
    path('delete_action/<int:pk>/', views.deleteUserAction, name='delete_action'),
    
]
