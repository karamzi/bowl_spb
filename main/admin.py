from django.contrib import admin
from .models import Img, Documents, Profile, Results
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    not_superuser_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_fieldsets(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return self.not_superuser_fieldsets
        return super().get_fieldsets(request, obj)


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
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
