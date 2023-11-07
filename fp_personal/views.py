from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from fp_blog.models import Article
from .models import UserProfile, UserFavourite, UserAction
from .forms import UserProfileForm, UserFavouriteForm, UserActionForm

# Create your views here.

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Do something for authenticated users.
            queryset = UserProfile.objects.filter(user=request.user.id)
            user_profile = get_object_or_404(UserProfile, user=request.user.id)
            return render(
            request,
            "my_planner.html",
            {
             "user": user_profile.user,
             "first_name":  request.user.first_name,
             "last_name": request.user.last_name,
             "email": request.user.email,
             "profile_image": user_profile.profile_image,
             "birth_year": user_profile.birth_year,
             "age_approx":  user_profile.age_approx,
             "age_exact":  user_profile.age_exact,
             "created_on" : user_profile.created_on,
#             "last_login" : request.user.last_login.day + (100 * request.user.last_login.month) + 10000 * (request.user.last_login.year)
              "last_login" : request.user.last_login,
             
             
            },
        )

        else:
            # Do something for anonymous users.
            console.log("User not logged in")

# comment out this next lot of code while I have a think about it        
#        if (UserProfile.objects.(id=request.user.id).exists())
#        queryset = UserProfile.objects.filter(id=request.user.id)
#        article = get_object_or_404(queryset, slug=slug)
#        comments = article.comments.filter(approved=True).order_by(
#            '-created_on')
#        actions = article.actions.order_by('action_seq')
#        liked = False
#        if article.likes.filter(id=self.request.user.id).exists():
#            liked = True
#        commented = False
#        print('User ', self.request.user.id)
#        if article.comments.filter(id=self.request.user.id).exists():
#            print('Unapproved comments exist for this user!')
#            commented = True

#        return render(
#            request,
#            "article_detail.html",
#            {
#             "article": article,
#             "comments": comments,
#             "commented": commented,
#             "actions": actions,
#             "liked": liked,
#             "comment_form": CommentForm()
#             },
#        )

#    def post(self, request, slug, *args, **kwargs):
#        queryset = Article.objects.filter(status=1)
#        article = get_object_or_404(queryset, slug=slug)
#        comments = article.comments.filter(approved=True).order_by(
#            '-created_on')
#        actions = article.actions.order_by('action_seq')
#        liked = False
#        if article.likes.filter(id=self.request.user.id).exists():
#            liked = True
#        comment_form = CommentForm(data=request.POST)
#        if comment_form.is_valid():
#            comment_form.instance.email = request.user.email
#            comment_form.instance.name = request.user.username
#            comment = comment_form.save(commit=False)
#            comment.article = article
#            comment.save()
#        else:
#            comment_form = CommentForm()
#
#        return render(
#                    request,
#                    "article_detail.html",
#                    {
#                        "article": article,
#                        "comments": comments,
#                        "commented": True,
#                        "comment_form": CommentForm(),
#                        "liked": liked,
#                        "actions": actions,
#                    },
#                    )


class ArticleFavourite(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.favourites.filter(id=request.user.id).exists():
            article.favourites.remove(request.user)
        else:
            article.favourites.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))
