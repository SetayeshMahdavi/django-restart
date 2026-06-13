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



def single_blog (request):
    return render(request,"blog/blog-single.html")


