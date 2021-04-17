from django.contrib import admin
from .models import Tournaments, Years, Calendar, Regulation, Results
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from main.admin import TournamentImgAdmin, TournamentDocumentsAdmin


class TournamentAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

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
    list_display = ('name', 'date')
    list_display_links = ('name', )
    search_fields = ('name',)
    inlines = [TournamentImgAdmin, TournamentDocumentsAdmin]
    form = TournamentAdminForm


class YearsAdmin(admin.ModelAdmin):
    list_display = ('year', 'rating')
    list_display_links = ('year', 'rating')


admin.site.register(Tournaments, TournamentAdmin)
admin.site.register(Years, YearsAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Regulation, RegulationsAdmin)
admin.site.register(Results)
