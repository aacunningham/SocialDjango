from django.contrib import admin
from Posts.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['owner', 'body', 'time']
    readonly_fields = ['time',]

admin.site.register(Post, PostAdmin)
