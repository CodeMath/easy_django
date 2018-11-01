from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class SummernoteBoard(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Board,SummernoteBoard)

admin.site.register(Reply)