from django.shortcuts import render
from django .http import HttpResponse
from .models import *


def blog (request):
    posts = Post.objects.filter(
        status=True
    ).order_by('-published_date')



    context = {
        'posts': posts
    }
    
    return render(request, 'blog/blog-home.html', context)



def single_blog (request, post_id):
    post = Post.objects.get(id=post_id)
    post.counted_views += 1
    post.save()

    context = {
        'post': post
    }

    return render(request, "blog/blog-single.html", context)

