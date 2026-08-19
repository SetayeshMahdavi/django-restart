from django.urls import path
from blog.views import *
from .feeds import LatestPostsFeed

app_name="blog"


urlpatterns = [
    path('', blog,name="blog"),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('<int:post_id>/',single_blog,name="single"),
]
 