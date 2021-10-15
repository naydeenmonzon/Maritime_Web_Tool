from django.contrib.admin import AdminSite

from django.contrib import admin
from django.forms import ModelForm
from django.urls import path
from .models import TOOLS



admin.site.register(TOOLS)

class URLS(admin.ModelAdmin):
    list_display = ('urlNAME', 'test')