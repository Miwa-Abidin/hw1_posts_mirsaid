from django.contrib import admin

from . models import Tweet, Comment, Mark

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Mark)