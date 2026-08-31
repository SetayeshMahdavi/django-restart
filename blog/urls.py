from django.urls import path
from blog.views import *

app_name="blog"


urlpatterns = [
    path('', blog,name="blog"),
    path('<int:post_id>/',single_blog,name="single"),
]