from django.contrib import admin
from .models import Tournaments, Years, Calendar, Regulation


admin.site.register(Tournaments)
admin.site.register(Years)
admin.site.register(Calendar)
admin.site.register(Regulation)
