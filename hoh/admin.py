from .models import *
from django.contrib import admin


class contestant_infoAdmin(admin.ModelAdmin):
    class Meta:
        model = contestant_info
class feedbackAdmin(admin.ModelAdmin):
	class Meta:
		model = feedback
admin.site.register(contestant_info,contestant_infoAdmin)
admin.site.register(feedback,feedbackAdmin)