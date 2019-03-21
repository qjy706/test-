from django.contrib import admin

# Register your models here.

from .models import *

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    list_display_links = ('name',)
    search_fields = ('name','age')

    list_filter = ('name','age')





admin.site.register(Teachers)