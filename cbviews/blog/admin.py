from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . import models


@admin.register(models.PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish']
    fields = ['title', 'slug', 'content', 'publish','view_count','publish_date','author_email','post_age']
    list_filter = ['title']
    search_fields = ['title']
    readonly_fields = ['slug','post_age','updated','timestamp']

    def post_age(self, obj, *args, **kwargs):
    	return str(obj.age)