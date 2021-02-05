from django.contrib import admin
from .models import Tournaments, Years, Calendar, Regulation
from django import forms
from ckeditor.widgets import CKEditorWidget


class TournamentAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = Tournaments
        fields = '__all__'


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('competition', 'city', 'date_start', 'date_finish')
    list_display_links = ('competition', 'city', 'date_start', 'date_finish')


class RegulationsAdmin(admin.ModelAdmin):
    list_display = ('year', 'name')
    list_display_links = ('year', 'name')


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'date')
    list_display_links = ('name', 'short_description')
    search_fields = ('name',)
    form = TournamentAdminForm


admin.site.register(Tournaments, TournamentAdmin)
admin.site.register(Years)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Regulation, RegulationsAdmin)
