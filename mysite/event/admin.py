from django.contrib import admin

from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_start')
    list_display_links = ('id', 'title')

class EventUserAdmin(admin.ModelAdmin):
    list_display = ('date_join', 'user_id')


admin.site.register(Event, EventAdmin)
admin.site.register(EventUser, EventUserAdmin)
