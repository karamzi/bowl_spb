from django.db import models
from datetime import datetime
from os.path import splitext
from tournaments.models import Results, Regulation


def img_path(instance, filename):
    return 'news/%s_%s%s' % (instance.pk, datetime.now().timestamp(), splitext(filename)[1])


class News(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название новости')
    short_description = models.TextField(max_length=255, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    tournament_results = models.ForeignKey(Results, on_delete=models.PROTECT, verbose_name='Результаты',
                                           related_name='news_results', null=True, blank=True)
    regulations = models.ForeignKey(Regulation, on_delete=models.CASCADE, verbose_name='Регламент',
                                    related_name='news_regulation', null=True, blank=True)
    news_image = models.ImageField(verbose_name='Изображение новости', upload_to=img_path, null=True, blank=True)
    count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']
