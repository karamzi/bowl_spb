from django.contrib import admin
from .models import NewsImg, NewsDocuments, TournamentDocuments, TournamentImg, Profile, Results, StudentsTournaments


class NewsImgAdmin(admin.TabularInline):
    model = NewsImg
    extra = 1


class NewsDocumentsAdmin(admin.TabularInline):
    model = NewsDocuments
    extra = 1


class TournamentImgAdmin(admin.TabularInline):
    model = TournamentImg
    extra = 1


class TournamentDocumentsAdmin(admin.TabularInline):
    model = TournamentDocuments
    extra = 1


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'player', 'results')
    list_display_links = ('tournament', 'player', 'results')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'rang')
    list_display_links = ('name', 'rang')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(StudentsTournaments)
