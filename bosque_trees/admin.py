from django.contrib import admin
from bosque_trees.models import Tree


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('code', 'latitude', 'longitude', 'species')
    search_fields = ('code', 'species')
    list_filter = ('species',)
    ordering = ('code',)
    list_per_page = 20
