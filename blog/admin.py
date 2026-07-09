from django.contrib import admin
from blog.models import Post , Category, Profile


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ['user__username']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)