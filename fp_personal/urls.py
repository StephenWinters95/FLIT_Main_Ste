from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='my_planner'),
#    path('<slug:slug>/', views.UserAction.as_view(), name='article_detail'),
#    path('like/<slug:slug>', views..as_view(), name='article_like'),
]
