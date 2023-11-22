from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Comment, Action
from .forms import CommentForm, UserCommentForm

# 21/11/23 DMcC The below code no longer needed 
#class ArticleList(generic.ListView):
#    model = Article
#    queryset = Article.objects.filter(status=1).order_by('-updated_on')
#    template_name = 'index.html'
#    paginate_by = 8

def ArticleList(request):
    # DMcC 21/11/23 Function-based article retrieval to faciliate tag-search
        
    queryset = Article.objects.filter(status=1).order_by('-updated_on')
    
    # DMcC 21/11/23 If the user has given a search term then check this filter
    search_post = request.GET.get('search')
    if search_post:
        queryset = queryset.filter(Q(content__icontains=search_post))

#   DMcC 21/11/23 pagination text taken from testdrive.io/blog/django-pagination for fbv    
    page_num = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4) #articles per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is our of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page_obj': page_obj})

class ArticleSearch(generic.ListView):
    # DMcC 21/11/23 the below search field text from stackoverflow.com re adding a search field #
#    def dynamic_articles_view(request):
#        context['object_list'] = article.objects.filter(tags__icontains=request.GET.get('search'))
 #       Print("In dynamic_articles_view")
#        return render(request, "index.html", context)
    model = Article
    queryset1 = Article.objects.filter(status=1).order_by('-updated_on')
    queryset = queryset1.filter(tags=3)
    template_name = 'index.html'
    
class ArticleDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')
        actions = article.actions.order_by('action_seq')
        number_of_actions = actions.count()

        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if article.favourites.filter(id=self.request.user.id).exists():
            bookmarked = True

        commented = False
        commented_unapproved = False
        print('User ', self.request.user.id)
        if article.comments.filter(id=self.request.user.id).exists():
            commented = True
            if article.comments.filter(id=self.request.user.id,
                                       approved=False).exists():
                print('Unmoderated responses exist for this user')
                commented_unapproved = True
        return render(
                      request,
                      "article_detail.html",
                      {
                       "article": article,
                       "comments": comments,
                       "commented": commented,
                       "commented_unapproved": commented_unapproved,
                       "actions": actions,
                       "number_of_actions": number_of_actions,
                       "liked": liked,
                       "bookmarked": bookmarked,
                       "comment_form": CommentForm()
                      },
                     )

    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')
        actions = article.actions.order_by('action_seq')
        number_of_actions = actions.count()
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if article.favourites.filter(id=self.request.user.id).exists():
            bookmarked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
                    request,
                    "article_detail.html",
                    {
                        "article": article,
                        "comments": comments,
                        "commented": True,
                        "commented_unapproved": True,
                        "comment_form": CommentForm(),
                        "liked": liked,
                        "bookmarked": bookmarked,
                        "actions": actions,
                        "number_of_actions": number_of_actions,
                       
                    },
                    )


# This is used when article is liked/unliked
# from within the article detail page
class ArticleLike(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


# This is used when article is liked/unliked
# from within the index/article summary page
# DMcC 15/11/23 this still needs some work as the
# user is currently returned to the article detail page after like/unlike
class ArticleSummaryLike(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        number_of_actions = article.actions.count()
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

# DMcC 18/11/23 want to play around with a render rather than a return
# statement at the endof this logic,
# could ths be used to return to the index page
# when this option is taken from the index page to start with?
            return render(
                          request,
                          "index.html",
                          {
                           "article": article,
                           "comments": comments,
                           "comment_count": comments.count,
                           "commented": commented,
                           "actions": actions,
                           "number_of_actions": number_of_actions,
                           "liked": liked,
                           "bookmarked": bookmarked,
                          },
                         )


# This is used when article is bookmarked/unbookmarked
# from within the index/article summary OR article detail page
# DMcC 15/11/23 this still needs some work as the user is currently
#  returned to the article detail page after bookmarking
class ArticleBookmark(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.favourites.filter(id=request.user.id).exists():
            article.favourites.remove(request.user)
            messages.add_message(request, messages.SUCCESS,
                                 "Article removed from your Reading List")
        else:
            article.favourites.add(request.user)
            messages.add_message(request, messages.SUCCESS,
                                 "Article added to your Reading List")
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class ArticleComment(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')

        return render(
                      request,
                      "index.html",
                      {
                       "article": article,
                       "comments": comments,
                       "comment_count": comments.count,
                       "commented": commented,
                       "actions": actions,
                       "liked": liked,
                       "bookmarked": bookmarked,
                      },
            )


def error_400(request, exception):
        data = {}
        return render(request,'400.html', data)

def error_403(request, exception):
        data = {}
        return render(request,'403.html', data)

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request, *args, **argv):
    return render(request,'500.html', status=500)
