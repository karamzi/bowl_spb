from django.contrib import admin
from .models import Img, Documents, Profile, Results, StudentsTournaments
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.is_superuser = False
        super().save_model(request, obj, form, change)


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
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
