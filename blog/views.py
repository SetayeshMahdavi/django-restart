from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, F, Q
from django.contrib import messages
from .models import *
from .forms import CommentForm


def blog (request):
    posts = Post.objects.filter(
        status=True
    ).order_by('-published_date').annotate(
        comment_count=Count('comments', filter=Q(comments__active=True, comments__parent__isnull=True))
    )


    categories = Category.objects.annotate(
        post_count=Count('post')
    )

    latest_post = posts.first()
    author = latest_post.author if latest_post else None

    context = {
        'posts': posts ,
        'categories': categories,
        'author': author,
    }
    
    return render(request, 'blog/blog-home.html', context)



def single_blog (request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.counted_views = F('counted_views') + 1
    post.save(update_fields=['counted_views'])


    categories = Category.objects.annotate(
        post_count=Count('post')
    )
    

    next_post = Post.objects.filter(
        status=True,
        published_date__gt=post.published_date
    ).order_by('published_date').first()



    prev_post = Post.objects.filter(
        status=True,
        published_date__lt=post.published_date
    ).order_by('-published_date').first()

    comments = post.comments.filter(active=True, parent__isnull=True).prefetch_related('replies')

    reply_to = request.GET.get('reply_to')
    reply_to = int(reply_to) if reply_to and reply_to.isdigit() else None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, "You must login to comment.")
            return redirect('blog:single', post_id=post.id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            parent_id = request.POST.get('parent')
            if parent_id:
                parent = Comment.objects.filter(id=parent_id, post=post).first()
                if parent:
                    comment.parent = parent
            comment.save()
            messages.success(request, "Your comment has been posted.")
            return redirect('blog:single', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'categories': categories,
        'next_post': next_post,
        'prev_post': prev_post,
         'author': post.author,
        'comments': comments,
        'form': form,
        'reply_to': reply_to,
    }

    return render(request, "blog/blog-single.html", context)

