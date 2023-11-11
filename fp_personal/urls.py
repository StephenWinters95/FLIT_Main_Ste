from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='my_planner'),
    path('myactions', views.UserActionView.as_view(), name='my_actions')
]
