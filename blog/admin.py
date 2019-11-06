from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'content']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
