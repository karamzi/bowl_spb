from django.contrib import admin
from .models import NewsTournamentDocuments, NewsTournamentsImg, Profile, Results


admin.site.register(NewsTournamentsImg)
admin.site.register(NewsTournamentDocuments)
admin.site.register(Profile)
admin.site.register(Results)

