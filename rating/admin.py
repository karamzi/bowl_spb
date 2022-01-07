from django.contrib import admin
from .models import Rating, Statistics, AllRating


class RatingAdmin(admin.ModelAdmin):
    list_display = ('player', 'league', 'score', 'active')
    list_display_links = ('player', 'league', 'score')
    list_editable = ('active',)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('year', 'name', 'mean', 'summ')
    list_display_links = ('year', 'name', 'mean', 'summ')


class AllRatingAdmin(admin.ModelAdmin):
    list_display = ('year', 'sex', 'rating')
    list_display_links = ('year', 'sex', 'rating')


admin.site.register(Rating, RatingAdmin)
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(AllRating, AllRatingAdmin)
