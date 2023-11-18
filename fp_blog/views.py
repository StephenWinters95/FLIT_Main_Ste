from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages 
from .models import Article, Comment, Action
from .forms import CommentForm, UserCommentForm

class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'
    paginate_by = 8

class ArticleDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')
        actions = article.actions.order_by('action_seq')
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
            if article.comments.filter(id=self.request.user.id, approved=False).exists():
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
 # DMcC 14/11/23 this next line is significant as it was saying that comment has no user
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
                        "bookmarked" : bookmarked,
                        "actions": actions,
                    },
                    )

# This is used when article is liked/unliked from within the article detail page
# DMcC 16/11/23 this needs more work as lik/unlike has stopped working from detail page???
class ArticleLike(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))

# This is used when article is liked/unliked from within the index/article summary page
# DMcC 15/11/23 this still needs some work as the user is currently returned to the article detail page after like/unlike
class ArticleSummaryLike(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
        
# DMcC 18/11/23 want to play around with a render rather than a retur statement at the endof this logic, 
# could ths be used to retur to the index page when this option is taken from the index page to start with?
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

# This is used when article is bookmarked/unbookmarked from within the index/article summary OR article detail page
# DMcC 15/11/23 this still needs some work as the user is currently returned to the article detail page after bookmarking
class ArticleBookmark(View):
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.favourites.filter(id=request.user.id).exists():
            article.favourites.remove(request.user)
            messages.add_message(request, messages.SUCCESS, "Article removed from your Reading List")
        else:
            article.favourites.add(request.user)
            messages.add_message(request, messages.SUCCESS, "Article added to your Reading List")
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

