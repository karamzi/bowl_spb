from django.db import models
from datetime import datetime
from os.path import splitext


def regulation_path(instance, filename):
    return 'regulation/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def statistic_path(instance, filename):
    return 'statistic/%s_%s%s' % (instance.year, datetime.now().timestamp(), splitext(filename)[1])


def rating_path(instance, filename):
    return 'rating/%s_%s%s' % (instance.year, datetime.now().timestamp(), splitext(filename)[1])


class Years(models.Model):
    year = models.SmallIntegerField(verbose_name='Год')
    statistic = models.FileField(verbose_name='Статистика', upload_to=statistic_path, blank=True, null=True)
    rating = models.FileField(verbose_name='Рейтинг', upload_to=rating_path, blank=True, null=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Общая статистика'
        ordering = ['-year']


class Regulation(models.Model):
    year = models.ForeignKey(Years, related_name='regulations', verbose_name='Год', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name='Название документа')
    file = models.FileField(verbose_name='Регламент', upload_to=regulation_path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регламент'
        verbose_name_plural = 'Регламенты'
        ordering = ['-year']


class Tournaments(models.Model):
    year = models.ForeignKey(Years, verbose_name='Год', on_delete=models.PROTECT, related_name='tournament_year')
    name = models.CharField(max_length=50, verbose_name='Название Турнира')
    short_description = models.TextField(max_length=100, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    regulation = models.OneToOneField(Regulation, on_delete=models.CASCADE, verbose_name='Регламент', null=True,
                                      blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-date']


class Calendar(models.Model):
    competition = models.CharField(max_length=50, verbose_name='Название турнира')
    city = models.CharField(max_length=20, verbose_name='Город проведения')
    status = models.CharField(max_length=10, verbose_name='Статус соревнований', blank=True)
    date_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата окончания')
    regulation = models.OneToOneField(Regulation, on_delete=models.CASCADE, verbose_name='Регламент', null=True,
                                      blank=True)

    def __str__(self):
        return self.competition

    class Meta:
        verbose_name = 'турнир'
        verbose_name_plural = 'Календарь турниров'
        ordering = ['date_start']
