from django.contrib import admin
from bosque_trees.models import Tree


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('accession', 'familyname', 'calcfullname', 'vernacularname', 'latitude', 'longitude')
    search_fields = ('accession', 'calcfullname', 'vernacularname')
    list_filter = ('calcfullname',)
    ordering = ('accession',)
    list_per_page = 20
