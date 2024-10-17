from . import views
from django.urls import path

# paths within the fp_blog app
urlpatterns = [
    path('', views.ArticleList, name='home'),
    path('maint/', views.maint_articles, name='maint_articles'),
    path('maint_users/', views.maint_users, name='maint_users'),  #added Ste 15/10/24
    path('add_user/', views.add_user, name='add_user'), # added Ste 16/10/24
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),  # added Ste 16/10/24
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'), # added Ste 16/10/24
    path('preview_user/<int:user_id>/', views.user_preview, name='user_preview'), # added Ste 16/10/24
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:id>/', views.delete_article, name='delete_article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('preview/<int:article_id>/', views.article_preview, name='article_preview'),
    path('bookmark/<slug:slug>', views.ArticleBookmark.as_view(),
         name='article_bookmark'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('comment/<slug:slug>', views.ArticleComment.as_view(),
         name='article_comment'),
    ]

# Error handlers for site errors
handler404 = 'fp_blog.views.error_404'
handler500 = 'fp_blog.views.error_500'
handler403 = 'fp_blog.views.error_403'
handler400 = 'fp_blog.views.error_400'
