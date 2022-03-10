from operator import imod
from django.contrib import admin

# Register your models here.
from .models import Headquarters, Contact

class HeadquartersAdmin(admin.ModelAdmin):
    list_display = [
        'address',
    ]

admin.site.register(Headquarters, HeadquartersAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
    ]

admin.site.register(Contact, ContactAdmin)