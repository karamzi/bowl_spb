from django.contrib import admin
from .models import Tournaments, Years, Calendar, Regulation
from django import forms
from ckeditor.widgets import CKEditorWidget


class TournamentAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = Tournaments
        fields = '__all__'


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'date')
    list_display_links = ('name', 'short_description')
    search_fields = ('name',)
    form = TournamentAdminForm


admin.site.register(Tournaments, TournamentAdmin)
admin.site.register(Years)
admin.site.register(Calendar)
admin.site.register(Regulation)
