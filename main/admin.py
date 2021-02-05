from django.contrib import admin
from .models import NewsTournamentDocuments, NewsTournamentsImg, Profile, Results


class NewsTournamentsImgAdmin(admin.ModelAdmin):
    list_display = ('news', 'tournament', 'name')
    list_display_links = ('news', 'tournament', 'name')


class NewsTournamentDocumentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'news', 'tournament')
    list_display_links = ('name', 'news', 'tournament')


admin.site.register(NewsTournamentsImg, NewsTournamentsImgAdmin)
admin.site.register(NewsTournamentDocuments, NewsTournamentDocumentsAdmin)
# admin.site.register(Profile)
# admin.site.register(Results)
