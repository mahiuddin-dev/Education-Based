from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# # Register your models here.
from .models import Job_Post, Job_Comment

# PostAdmin
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
    ]
    summernote_fields = ('body',)
    prepopulated_fields = {'slug': ['title', ]}

admin.site.register(Job_Post, PostAdmin)


# CommentAdmin
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]
    actions = ['approve_comment']

    def approve_comment(self,request,queryset):
        queryset.update(approve=True)

admin.site.register(Job_Comment, CommentAdmin)