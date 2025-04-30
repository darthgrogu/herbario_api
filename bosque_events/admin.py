from django.contrib import admin
from bosque_events.models import TreeEvent


@admin.register(TreeEvent)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('tree', 'event_type', 'event_date', 'description')
