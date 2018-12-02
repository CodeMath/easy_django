from django.contrib import admin
from .models import *

# class history_admin(admin.ModelAdmin):
#     list_display = ["name","asks","bids","asks_vol",'bids_vol','date']
#     list_filter = ["name","date"]
#
#
# admin.site.register(History, history_admin)

@admin.register(History)
class history_admin(admin.ModelAdmin):
    list_display = ["name", "asks", "bids", "asks_vol", 'bids_vol', 'date']
    list_filter = ["name", "date"]