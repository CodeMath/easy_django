from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Reward)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Funding,PostAdmin)
admin.site.register(Funding_News)
