from django.db import models
from main.models import Profile
from tournaments.models import Years


class Rating(models.Model):
    LEAGUE = (
        ('man', 'Мужчины'),
        ('woman', 'Женщины'),
    )
    player = models.OneToOneField(Profile, verbose_name='Спортсмен', on_delete=models.PROTECT)
    score = models.SmallIntegerField(verbose_name='Очки')
    active = models.BooleanField(default=False, verbose_name='Активный')
    league = models.TextField(choices=LEAGUE, verbose_name='Лига')

    def __str__(self):
        return self.player.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        ordering = ['league', '-score']


class Statistics(models.Model):
    name = models.OneToOneField(Profile, on_delete=models.PROTECT, verbose_name='Спортсмен')
    year = models.ForeignKey(Years, on_delete=models.PROTECT, verbose_name='Год', null=True, blank=True,
                             related_name='statistic_year')
    mean = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Средний', default=0)
    min = models.SmallIntegerField(verbose_name='Минимальная игра', default=300)
    max = models.SmallIntegerField(verbose_name='Максимальная игра', default=0)
    score = models.SmallIntegerField(verbose_name='Количество игр', default=0)
    summ = models.SmallIntegerField(verbose_name='Сумма', default=0)

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = 'Статистику'
        verbose_name_plural = 'Статистика'
        ordering = ['-year']
