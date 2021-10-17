from django.db import models
from datetime import datetime
from os.path import splitext


def regulation_path(instance, filename):
    return 'regulation/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def statistic_path(instance, filename):
    return 'statistic/%s_%s%s' % (instance.year, datetime.now().timestamp(), splitext(filename)[1])


def rating_path(instance, filename):
    return 'rating/%s_%s%s' % (instance.year, datetime.now().timestamp(), splitext(filename)[1])


def results_path(instance, filename):
    return 'results/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def img_path(instance, filename):
    return 'reports/%s_%s%s' % (instance.pk, datetime.now().timestamp(), splitext(filename)[1])


class Years(models.Model):
    year = models.SmallIntegerField(verbose_name='Год')
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
    archive = models.BooleanField(verbose_name='Архив', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регламент'
        verbose_name_plural = 'Регламенты'
        ordering = ['-year']


class Tournaments(models.Model):
    year = models.ForeignKey(Years, verbose_name='Год', on_delete=models.PROTECT, related_name='tournament_year')
    name = models.CharField(max_length=50, verbose_name='Название Турнира')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-date']


class Reports(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название Турнира')
    short_description = models.TextField(max_length=255, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE, verbose_name='Регламент', null=True,
                                   blank=True, related_name='regulation')
    tournament_results = models.ForeignKey('Results', verbose_name='Результаты', on_delete=models.CASCADE, null=True,
                                           related_name='tournament_results', blank=True)
    report_image = models.ImageField(verbose_name='Изображение новости', upload_to=img_path, null=True, blank=True)
    count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
        ordering = ['-date']


class Calendar(models.Model):
    TYPE = (
        ('Sport', 'Спортивный'),
        ('Student', 'Студенческий'),
    )
    competition = models.CharField(max_length=50, verbose_name='Название турнира')
    city = models.CharField(max_length=20, verbose_name='Город проведения')
    status = models.CharField(max_length=50, verbose_name='Статус соревнований', blank=True)
    date_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата окончания')
    type = models.CharField(max_length=20, verbose_name='Тип турнира', choices=TYPE, default='Sport')
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE, verbose_name='Регламент', null=True,
                                   blank=True)

    def __str__(self):
        return self.competition

    class Meta:
        verbose_name = 'турнир'
        verbose_name_plural = 'Календарь турниров'
        ordering = ['date_start']


class Results(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название турнира')
    file = models.FileField(upload_to=results_path, verbose_name='Результаты', blank=True, null=True)
    link = models.CharField(max_length=300, verbose_name='Ссылка на результаты', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        ordering = ['-date']
