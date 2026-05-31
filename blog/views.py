from django.shortcuts import render
from django .http import HttpResponse


def blog (request):
    return render(request,"blog/blog-home.html")



def single_blog (request):
    return render(request,"blog/blog-single.html")


