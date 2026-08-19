from django.contrib import admin
from blog.models import *


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'message', 'parent', 'active', 'created_date')
    readonly_fields = ('author', 'created_date')
    can_delete = True


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'comment_count', 'status', 'published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']
    inlines = [CommentInline]

    @admin.display(description='Comments')
    def comment_count(self, obj):
        return obj.comments.count()


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ['user__username']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'parent', 'active', 'created_date')
    list_filter = ('active', 'created_date')
    search_fields = ['author__username', 'message']
    actions = ['approve_comments']

    @admin.action(description='Approve selected comments')
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)