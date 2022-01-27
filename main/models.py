from django.db import models
from datetime import datetime
from os.path import splitext
from news.models import News
from tournaments.models import Reports, Tournaments, Years


def img_path(instance, filename):
    return 'img/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def document_path(instance, filename):
    return 'img/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


class Img(models.Model):
    news = models.ForeignKey(News, related_name='news_img', verbose_name='Новость', on_delete=models.CASCADE,
                             blank=True, null=True)
    tournament = models.ForeignKey(Reports, related_name='tournament_img', verbose_name='Новость',
                                   on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Подпись', blank=True, null=True)
    img = models.ImageField(verbose_name='Изображение', upload_to=img_path)
    width = models.SmallIntegerField(verbose_name='Ширина', default=300)
    height = models.SmallIntegerField(verbose_name='Высота', default=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Documents(models.Model):
    news = models.ForeignKey(News, related_name='news_document', verbose_name='Новость', on_delete=models.CASCADE,
                             blank=True, null=True)
    tournament = models.ForeignKey(Reports, related_name='tournament_document', verbose_name='Новость',
                                   on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, verbose_name='Название документа')
    file = models.FileField(verbose_name='Докумен', upload_to=document_path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Profile(models.Model):
    RANG = (
        ('', ''),
        ('мс', 'мс'),
        ('кмс', 'кмс'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    name = models.CharField(max_length=30, verbose_name='Спортсмен')
    rang = models.TextField(choices=RANG, verbose_name='Разряд', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ['name']


class Results(models.Model):
    tournament = models.ForeignKey(Tournaments, verbose_name='Турнир', on_delete=models.PROTECT, related_name='results')
    player = models.ForeignKey(Profile, verbose_name='Спортсмен', on_delete=models.PROTECT,
                               related_name='results_player')
    results = models.TextField(verbose_name='Результаты')

    def __str__(self):
        return self.player.name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты спортсменов'
        ordering = ['id']
