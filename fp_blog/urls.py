from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('bookmark/<slug:slug>', views.ArticleBookmark.as_view(), name='article_bookmark'),
]
