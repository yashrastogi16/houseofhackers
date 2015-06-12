from .models import *
from django.contrib import admin


class contestant_infoAdmin(admin.ModelAdmin):
    # list_display = ['username','location','email_id','date_time']
    # list_filter = ['date_time']
    # search_fields = ['date_time']
    class Meta:
        model = contestant_info

admin.site.register(contestant_info,contestant_infoAdmin)