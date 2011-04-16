from django.contrib import admin
from flyers.models import ForSaleFlyer, LostFlyer, Theme

class ThemeAdmin(admin.ModelAdmin):
	list_display = ('name', 'flyer_type')
	list_filter = ('flyer_type',)

admin.site.register(ForSaleFlyer)
admin.site.register(LostFlyer)
admin.site.register(Theme, ThemeAdmin)