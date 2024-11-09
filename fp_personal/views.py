from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from fp_blog.models import Article, Action, Comment
from cloudinary.models import CloudinaryField
from .models import UserProfile, UserAction, Feedback
from fp_blog.forms import ActionForm
from .forms import UserProfileForm, UserActionForm
# from rest_framework import serializers


# This is the main view for user profile n the my_planner link/ page
# it includes logic to summarise # of likes, bokmarks. actions etc
class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # this option is only valid for reg users not annonymous user

            if (UserProfile.objects.filter(user=request.user.id).exists()):
                # Can pickup user profile fields from db for authd users
                queryset = UserProfile.objects.filter(user=request.user.id)
                user_profile = get_object_or_404(UserProfile,
                                                 user=request.user)
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
                number_of_bookmarks = user_profile.number_of_bookmarks
                number_of_actions = user_profile.number_of_actions
                num_val_com = user_profile.number_of_valid_comments
                number_of_valid_comments = num_val_com
                user_profile = True
            else:
                # user has User but no UserProfile
                birth_year = 1900
                age_approx = 0
                age_exact = 0
                created_on = '01/01/1900'
                profile_image = "../static/images/placeholder.png"
                actions = []
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
                 "last_login": request.user.last_login,
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



# Create your views here.
# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
# @login_required
# DMcC 18/09/24 - added below from Jeweller project
def profile_detail(request, profile_id):
    """ A view to return a specific profile id """
    if ((request.user.is_authenticated
        and (profile_id == request.user.userprofile.id))
            or (request.user.is_superuser)):

        current_profile = get_object_or_404(UserProfile, id=profile_id)
        # removed the message below as it appears only when the button is
        # pressed, and is confusing to the user
        # messages.info(request, (f'Editing user profile
        # for {current_profile.user}'))

        if request.method == 'POST':
            # user_form = CustomSignupForm(request.POST, request.FILES or None,
            # instance=current_user)
            profile_form = UserProfileForm(request.POST, request.FILES or None,
                                           instance=current_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect(reverse('profile_detail',
                                        args=[current_profile.id]))
            else:
                messages.error(request, 'Update failed. Please ensure '
                               + 'the form is valid.')
        else:
            profile_form = UserProfileForm(instance=current_profile)

        template = 'profiles/profile.html'
        context = {
            'form': profile_form,
            'on_profile_page': True,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Restricted: Must have SysAdmin rights to edit'
                       + ' other users profile!')
        return redirect(reverse('home'))




# ArticleBookmark is designed to toggle on/off bookmark favourites for a user
# and returns the user to the article detail view
class ArticleBookmark(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.favourites.filter(id=request.user.id).exists():
            article.favourites.remove(request.user)
        else:
            article.favourites.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


# UserActionList retrieves the task list for the current logged-in user
# and returns list of tasks, and count of tasks
class UserActionList(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = request.user.user_actions
            number_of_actions = queryset.count()
            user_actions = queryset.order_by('user_action_seq',
                                             'created_on')
            return render(
                    request,
                    "my_actions.html",
                    {
                     "number of actions ": number_of_actions,
                     "user_actions": user_actions, }
                    )
        else:
            console.log("User not logged in")


# class UserActionView is used to present and manipulate a User Task (Action)
class UserActionView(View):
    queryset = UserAction.objects.all()

    def get(self, request):
        """ returns a list of user actions for a particular user """
        user_actions_unorder = UserAction.objects.filter(user=request.user.id)
        user_actions = user_actions_unorder.order_by('user_action_seq',
                                                     'created_on')

    def next_seq(request):
        """ This function retrieves the list of user actions for a user """
        """ sorts by seq num, and increments highest valueby 10 """
        exist_acts = UserAction.objects.filter(user=request.user.id).exists()
        if exist_acts:
            queryset_unorder = UserAction.objects.filter(user=request.user.id)
            queryset = queryset_unorder.order_by('-user_action_seq')
            max_seq = queryset[0].user_action_seq
            next_seq = max_seq + 10
        else:
            next_seq = 10

        return next_seq

    def get(self, request, *args, **kwargs):
        """" returns a list of user actions """
        if (UserAction.objects.filter(user=request.user.id).exists()):
            queryset_unsorted = UserAction.objects.filter(user=request.user.id)
            queryset = queryset.order_by('user_action_seq', 'created_on')
            number_of_actions = queryset.count()

            return render(
                request,
                "my_actions.html",
                {
                 "Seq": user_action_seq,
                 "Date Created": created_on,
                 "From article": parent_article,
                 "Action": user_action_desc,
                 "URL": user_action_url,
                 "Done so far": user_action_taken,
                 "Result": observation,
                 "Completed": completed,
                 "Date": completed_on,
                }
                )


# This next set of code developed with inspriration from Dennis Ivy videos
#  Django 2021 Course Session #3 Models Forms & CRUD
# note function-based rather than class-cased coding
def createUserAction(request):
    """ Function createUserAction returns user action with next seq# """
    next_seq = UserActionView.next_seq(request)
    print('In CreateUserAction():  next_seq returned is: ', next_seq)
    form = UserActionForm(initial={"user": request.user.id,
                                   "user_action_seq": next_seq, })

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Personal Action # " + str(next_seq)
                                 + " created")
            return redirect('my_planner')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error on new action form")

    context = {'form': form}
    return render(request, 'my_actions.html', context)


# Function copyUserAction is used to copy an Article-based task (action)
# and create a new User-based task (action)
def copyUserAction(request, pk):
    """ parameters are request and article_pk"""
    """ returns a new action rendered to actions.html page """
    action = Action.objects.get(id=pk)
    action_desc = action.action_desc
    
    ('In copyUserAction():  source action_id is ', action.id,
          ' desc is ', action_desc)
    slug = action.article.slug
    form = ActionForm(instance=action)
    print('In copyUserAction():  copy-from article is ', action.article)
    print('In copyUserAction():  slug is ', slug)
    print('In copyUserAction():  copy-from action description is ',
          action.action_desc)

    next_seq = UserActionView.next_seq(request)
    print('In copyUserAction():  next_seq return from function is: ', next_seq)
    form = UserActionForm(initial={"user": request.user.id,
                                   "user_action_seq": next_seq,
                                   "parent_article": action.article,
                                   "user_action_desc": action.id,
                                   "user_action_url": action.action_url, })

    if request.method == 'POST':
        form = UserActionForm(request.POST)
        if form.is_valid():
            form.save()
            # DMcC 15/11/23 Add success message to confirm action is added
            messages.add_message(request, messages.SUCCESS,
                                 "Personal Action # " + str(next_seq)
                                 + " created")
            return redirect(reverse('article_detail', args=[slug]))

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
            # Add success message to confirm action is updated
            messages.add_message(request, messages.SUCCESS, "Action: #"
                                 + str(action.user_action_seq) + " -  "
                                 + str(action.user_action_desc) + " updated")
            return redirect('my_planner')

    context = {'form': form}
    return render(request, 'my_actions.html', context)


# Again this delete User Action is adapted from Dennis Ivy training viedos:
def deleteUserAction(request, pk):
    action = UserAction.objects.get(id=pk)

    if request.method == 'POST':
        action.delete()
        # DMcC 15/11/23 Add success message to confirm action is updated
        messages.add_message(request, messages.SUCCESS, "Personal Action # "
                             + str(action.user_action_seq) + " deleted")
        return redirect('my_planner')

    # DMcC 15/11/23 what is the below line return redirect already done?
    return render(request, 'delete.html', {'object': 'action '
                                           + str(action.user_action_seq)})


# DMcC 17/11/23 update User Profile - adapted from Dennis Ivy training videos:
def addUserProfile(request):
    print('In addUserProfile():  user is: ', request.user)
    profile_image = "../../static/images/placeholder.png"
    birth_year = 1900
    age_approx = 123
    age_exact = 123

#   user_profile = request.user.userprofile

    form = UserProfileForm(initial={"user": request.user.id,
                                    "profile_image": profile_image,
                                    "birth_year": birth_year,
                                    "age_approx": age_approx,
                                    "age_exact": age_exact})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User profile "
                                 + str(request.user) + " created")
            return redirect('my_planner')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error on new user profile form")
    context = {'form': form}
    return render(request, 'my_user.html', context)


# DMcC 17/11/23 update User Profile - adapted from Dennis Ivy training videos:
def updateUserProfile(request, pk):
    print('In addUserProfile():  user is: key ', pk, "user", request.user)
    user_profile = UserProfile.objects.get(id=pk)
    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Add success message to confirm action is updated
            messages.add_message(request, messages.SUCCESS,
                                 "User profile "+str(request.user)+" updated")
            return redirect('my_planner')

    context = {'form': form}
    return render(request, 'my_user.html', context)


# DMcC 15/11/23 The below no longer used
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('my_planner')
    return render(request, 'delete.html', {'object': 'comment '
                                           + str(comment.body)})


# DMcC 13/11/23 watch out - below code deletes article, rather than bookmark!!
# Removed from active functionality, bookmark now deleted via fp_blog article
def deleteBookmark(request, pk):
    bookmark = request.user.article_favourite.get(id=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('my_planner')

    return render(request, 'delete.html', {'object': 'bookmark to '
                  + str(bookmark)})





class FeedbackList(generic.ListView):
    model = Feedback
    queryset = Feedback.objects.order_by('-created_on')
    template_name = 'about.html'
    paginate_by = 8


def error_400(request, exception):
    """"error handling 400"""
    data = {}
    return render(request, '400.html', data)


def error_403(request, exception):
    """"error handling 403"""
    data = {}
    return render(request, '403.html', data)


def error_404(request, exception):
    """"error handling 404"""
    data = {}
    return render(request, '404.html', data)


def error_500(request, *args, **argv):
    """"error handling 500"""
    return render(request, '500.html', status=500)
