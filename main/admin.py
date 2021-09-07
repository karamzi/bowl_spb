from django.contrib import admin
from .models import Img, Documents, Profile, Results, StudentsTournaments


class NewsImgAdmin(admin.TabularInline):
    model = Img
    extra = 1
    exclude = ('tournament', 'type')


class NewsDocumentsAdmin(admin.TabularInline):
    model = Documents
    extra = 1
    exclude = ('tournament', 'type')


class TournamentImgAdmin(admin.TabularInline):
    model = Img
    extra = 1
    exclude = ('news', 'type')


class TournamentDocumentsAdmin(admin.TabularInline):
    model = Documents
    extra = 1
    exclude = ('news', 'type')


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'player', 'results')
    list_display_links = ('tournament', 'player', 'results')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'rang')
    list_display_links = ('name', 'rang')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(StudentsTournaments)
admin.site.register(Documents)
