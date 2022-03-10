from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import About

class AboutAdmin(SummernoteModelAdmin):
    list_display = [
        'company_name',
        'oppaning_date',
    ]
    summernote_fields = ('description',)

admin.site.register(About, AboutAdmin)

