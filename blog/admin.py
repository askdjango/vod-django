# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'
    # content_size.allow_tags = True  # deprecated

# admin.site.register(Post, PostAdmin)
