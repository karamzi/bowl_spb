from django.contrib import admin
from .models import Rating, Statistics


class RatingAdmin(admin.ModelAdmin):
    list_display = ('player', 'league', 'score', 'active')
    list_display_links = ('player', 'league', 'score')
    list_editable = ('active',)


admin.site.register(Rating, RatingAdmin)
# admin.site.register(Statistics)
