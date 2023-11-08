from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('bookmark/<slug:slug>', views.ArticleBookmark.as_view(), name='article_bookmark'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('like/<slug:slug>', views.ArticleSummaryLike.as_view(), name='article_summary_like'),
]  
