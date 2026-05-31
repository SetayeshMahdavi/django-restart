from django.contrib import admin
from website.models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject']
    search_fields=['name','subject']
    list_filter=['created_date']
    