from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F
from .models import *

def blog (request):
    posts = Post.objects.filter(
        status=True
    ).order_by('-published_date')

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

    context = {
        'post': post,
        'categories': categories,
        'next_post': next_post,
        'prev_post': prev_post,
         'author': post.author,
    }

    return render(request, "blog/blog-single.html", context)