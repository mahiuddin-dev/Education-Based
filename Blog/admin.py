from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# # Register your models here.
from .models import Blog_Post, Post_Comment, Category_List


# PostAdmin
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'category',
        'home_slider',
        'feature_news'
    ]
    summernote_fields = ('body',)
    prepopulated_fields = {'slug': ['title', ]}

admin.site.register(Blog_Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ]}

admin.site.register(Category_List, CategoryAdmin)

# CommentAdmin
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]
    actions = ['approve_comment']

    def approve_comment(self,request,queryset):
        queryset.update(approve=True)

admin.site.register(Post_Comment, CommentAdmin)