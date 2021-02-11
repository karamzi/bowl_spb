from django.contrib import admin
from .models import News
from django import forms
from ckeditor.widgets import CKEditorWidget
from main.admin import NewsImgAdmin, NewsDocumentsAdmin


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'date')
    list_display_links = ('name', 'short_description')
    search_fields = ('name',)
    inlines = [NewsImgAdmin, NewsDocumentsAdmin]
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
