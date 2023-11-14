from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from fp_blog.forms import ActionForm
from fp_blog.models import Article, Action, Comment
from .models import UserProfile, UserAction
# from .models import UserFavourite
from .forms import UserProfileForm, UserActionForm
# from .forms import UserProfileForm, UserFavouriteForm, UserActionForm
from rest_framework import serializers

# Create your views here.
# This is the main view for user profile n the my_planner link/ page
# it includes logic to summarise # of likes, bokmarks. actions etc 

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Do something for authenticated users.

            if (UserProfile.objects.filter(user=request.user.id).exists()):
                queryset = UserProfile.objects.filter(user=request.user.id)
                user_profile = get_object_or_404(UserProfile, user=request.user)
                user = get_object_or_404(User, id=request.user.id)
                actions = user.user_actions.filter(user=request.user)
                bookmarks = user.article_favourite.all()
                comments = user.user_comments.all()

                birth_year = user_profile.birth_year
                age_approx = user_profile.age_approx
                age_exact = user_profile.age_exact
                created_on = user_profile.created_on
                profile_image = user_profile.profile_image
                number_of_likes = user_profile.number_of_likes
                number_of_bookmarks=user_profile.number_of_bookmarks
                number_of_actions = user_profile.number_of_actions
                number_of_valid_comments = user_profile.number_of_valid_comments
                user_profile = True
            else:
                birth_year = 1900
                age_approx = 0
                age_exact = 0
                created_on = '01/01/1900'
                profile_image = "/static/images/placeholder.png"
                actions =[]
                comments = []
                bookmarks = []     
                number_of_likes = 0 
                number_of_bookmarks = 0          
                number_of_actions = 0
                number_of_valid_comments = 0
                user_profile = False
#            endif
            
            return render(
                request,
                "my_planner.html",
                {
                "user": request.user,
                "first_name":  request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "profile_image": profile_image,
                "birth_year": birth_year,
                "age_approx":  age_approx,
                "age_exact":  age_exact,
                "created_on": created_on,
                "last_login" : request.user.last_login,
                "number_of_likes": number_of_likes,
                "number_of_bookmarks": number_of_bookmarks,
                "number_of_valid_comments": number_of_valid_comments,
                "number_of_actions": number_of_actions,
                "actions": actions,
                "bookmarks": bookmarks,
                "comments": comments,
                "user_profile": user_profile,
                },
                )
        else:
            # Do something for anonymous users.
            console.log("User not logged in")

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

    def next_seq(request):
        existing_actions = queryset = UserAction.objects.filter(user=request.user.id).exists()
        if existing_actions:
            queryset = UserAction.objects.filter(user=request.user.id).order_by('-user_action_seq')
            latest_rec = UserAction.objects.order_by('-user_action_seq').filter(user_action_seq__in=queryset[:0])
        
            max_seq = queryset[0].user_action_seq
            next_seq = max_seq + 10
        else:
            next_seq = 10
        
        return next_seq

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
# note this is function-baed rather than class-cased coding so will probably need to be repa=laced with class-based equivalent 

def createUserAction(request):
    next_seq = UserActionView.next_seq(request)
    print('In CreateUserAction():  next_seq returned from function is: ', next_seq)
    form=UserActionForm(initial={"user":request.user.id, "user_action_seq": next_seq})

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('my_planner')

    context = {'form': form}
    return render(request, 'my_actions.html', context)

def copyUserAction(request, pk):
    action = Action.objects.get(id=pk)
    action_desc = action.action_desc
    slug = action.article.slug
    form = ActionForm(instance=action)
    print('In copyUserAction():  copy-from article is ', action.article)
    print('In copyUserAction():  slug is ', slug)
    print('In copyUserAction():  copy-from action description is ', action.action_desc)
    
    next_seq = UserActionView.next_seq(request)
    print('In copyUserAction():  next_seq returned from function is: ', next_seq)
    form=UserActionForm(initial={"user":request.user.id, "user_action_seq": next_seq, "parent_article": action.article, "user_action_desc": action.action_desc, "user_action_taken": action_desc, })

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect(reverse('article_detail',args=[slug]) )

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

def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('my_planner')
    return render(request, 'delete.html', {'object': 'comment ' + str(comment.body)})

# watch ut aas the code below deletes the article, rather than the bookmark!!!!        
def deleteBookmark(request, pk):
    bookmark = request.user.article_favourite.get(id=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('my_planner')
    
    return render(request, 'delete.html', {'object': 'bookmark to ' + str(bookmark)})
    