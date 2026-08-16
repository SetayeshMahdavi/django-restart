from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='authors/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"



class Category(models.Model ):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post (models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    image=models.ImageField(upload_to='blog/', blank=True, null=True)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return f"{self.title} (ID : {self.id})"

   


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"