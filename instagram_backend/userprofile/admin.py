from django.contrib import admin
from .models import Post, UserProfile, Story, Comment
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Story)
