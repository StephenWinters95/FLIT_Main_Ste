from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from fp_blog.models import Article, Action, Comment
from .models import UserProfile, UserAction
# from .models import UserFavourite
from .forms import UserProfileForm, UserActionForm
# from .forms import UserProfileForm, UserFavouriteForm, UserActionForm
from rest_framework import serializers


# Create your views here.

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Do something for authenticated users.

            if (UserProfile.objects.filter(user=request.user.id).exists()):
                queryset = UserProfile.objects.filter(user=request.user.id)
                user_profile = get_object_or_404(UserProfile, user=request.user)
                user = get_object_or_404(User, id=request.user.id)

                actions = user.user_actions.filter(user=request.user)

                bookmarks = User.article_favourite
                print(bookmarks)
                
                comments = User.user_comments
                print(comments)
#                queryset_comments = Article.comments.order_by(
#                '-created_on')
#                comments = queryset_comments.filter(user=request.user, approved=True)

                print(comments)

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
                "created_on": user_profile.created_on,
    #             "last_login" : request.user.last_login.day + (100 * request.user.last_login.month) + 10000 * (request.user.last_login.year)
                "last_login" : request.user.last_login,
                "number_of_likes": user_profile.number_of_likes,
                "number_of_bookmarks": user_profile.number_of_bookmarks,
                "number_of_valid_comments": user_profile.number_of_valid_comments,
                "number_of_actions": user_profile.number_of_actions,
                "actions": actions,
                },
                )
            else:
                return render(
                request,
                "my_planner.html",
                {
                "user": request.user,
                "first_name":  request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "profile_image": "static/images/placeholder.png",
                "birth_year": 1900,
                "age_approx":  0,
                "age_exact":  0,
                "created_on" : '01/01/1900',
    #             "last_login" : request.user.last_login.day + (100 * request.user.last_login.month) + 10000 * (request.user.last_login.year)
                "last_login" : request.user.last_login,
                },
                )
            endif
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


class ArticleBookmark(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.favourites.filter(id=request.user.id).exists():
            article.favourites.remove(request.user)
        else:
            article.favourites.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))

class UserActionList(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset= request.user.user_actions
            number_of_actions = queryset.count()
            user_actions = queryset.order_by('user_action_seq',
                'created_on')
    #       user_actions = UserAction.my_actions(self.request)
            return render (
                    request,
                    "my_actions.html",
                    {
                    "number of actions ": number_of_actions,
                    "user_actions": user_actions}
                    )
        else:
            console.log("User not logged in")


class UserActionList(View):
    model = UserAction
    def get(self, request, *args, **kwargs):
        user_actions = request.user.user_actions.order_by('user_action_seq',
            'created_on')
        number_of_actions = user_actions.count()
            
#       user_actions = UserAction.my_actions(self.request)
        return render (
                request,
                "my_actions.html",
                {
                "number of actions ": number_of_actions,
                "user_actions": user_actions}
                )

# the below no longer being activated due to struggles with composite dataset returned 11/11/23
class UserActionView(View):
    queryset = UserAction.objects.all()

    def get(self, request):
        user_actions = UserAction.objects.filter(user=request.user.id).order_by('user_action_seq', 'created_on')

    def get(self, request, *args, **kwargs):
        if (UserAction.objects.filter(user=request.user.id).exists()):
            queryset = UserAction.objects.filter(user=request.user.id).order_by('user_action_seq', 'created_on') 
            number_of_actions = queryset.count()
            
            return render(
                request,
                "my_actions.html",
                {
                "Seq": user_action_seq,
                "Date Created": created_on,
                "From article": parent_article,
                "Action": user_action_desc,
                "Done so far": user_action_taken,
                "Result": observation,
                "Completed": completed,
                "Date": completed_on,
                }
                )
            
class UserActionSerializer(serializers.Serializer):
    class Meta:
        model = UserAction
        fields = ['user', 'user_action_seq', 'parent_article', 'user_action_desc', 'user_action_taken', 'observation', 'user_action_date', 'user_action_type', 'completed', 'created_on', 'completed_on']

# This next set of code developed in parallel with Dennis Ivy videos so remember to refer bakc to there =- Django 2021 Course Session #3 Models Forms & CRUD

def createUserAction(request):
    form=UserActionForm()

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('my_planner')

    context = {'form': form}
    return render(request, 'my_actions.html', context)

# Again this update User Action is adapted from Dennis Ivy training viedos:

def updateUserAction(request, pk):
    action = UserAction.objects.get(id=pk)
    form = UserActionForm(instance=action)

    if request.method == 'POST':
        form = UserActionForm(request.POST, instance=action)
        if form.is_valid(): 
            form.save()
            return redirect('my_planner')

    context = {'form': form}
    return render(request, 'my_actions.html', context)


# Again this delete User Action is adapted from Dennis Ivy training viedos:

def deleteUserAction(request, pk):
    action = UserAction.objects.get(id=pk)

    if request.method == 'POST':
        action.delete()
        return redirect('my_planner')
    return render(request, 'delete.html', {'object': 'action ' + str(action.user_action_seq)})

        
 