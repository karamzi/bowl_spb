from django.db import models
from main.models import Profile
from tournaments.models import Years


class Rating(models.Model):
    LEAGUE = (
        ('men', 'Мужчины'),
        ('women', 'Женщины'),
    )
    player = models.OneToOneField(Profile, verbose_name='Спортсмен', on_delete=models.PROTECT)
    score = models.SmallIntegerField(verbose_name='Очки')
    league = models.TextField(choices=LEAGUE, verbose_name='Лига')

    def __str__(self):
        return self.player.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг топ 8'
        ordering = ['league', '-score']


class AllRating(models.Model):
    year = models.ForeignKey(Years, on_delete=models.PROTECT, verbose_name='Год', null=True, blank=True,
                             related_name='rating_year')
    SEX = (
        ('men', 'Мужчины'),
        ('women', 'Женщины'),
    )
    sex = models.CharField(max_length=5, verbose_name='Пол', choices=SEX, default='men')
    rating = models.TextField(verbose_name='Райтинг Json')

    def __str__(self):
        return f'Райтинг {self.year.year}года - {self.get_sex_display()}'

    class Meta:
        verbose_name = 'Полный рейтинг'
        verbose_name_plural = 'Полный рейтинг (для страницы рейтинг)'
        ordering = ['year']


class Statistics(models.Model):
    name = models.ForeignKey(Profile, related_name='statistic_profile', on_delete=models.PROTECT,
                             verbose_name='Спортсмен')
    year = models.ForeignKey(Years, on_delete=models.PROTECT, verbose_name='Год', null=True, blank=True,
                             related_name='statistic_year')
    SEX = (
        ('men', 'М'),
        ('women', 'Ж'),
    )
    sex = models.CharField(max_length=5, verbose_name='Пол', choices=SEX, default='men')
    mean = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Средний', default=0)
    min = models.SmallIntegerField(verbose_name='Минимальная игра', default=300)
    max = models.SmallIntegerField(verbose_name='Максимальная игра', default=0)
    score = models.SmallIntegerField(verbose_name='Количество игр', default=0)
    games_more_200 = models.SmallIntegerField(verbose_name='Количество игр за 200', default=0)
    mean_games_more_200 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Игр за 200 (процент)',
                                              default=0)
    summ = models.SmallIntegerField(verbose_name='Сумма', default=0)

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = 'Статистику'
        verbose_name_plural = 'Персональная статистика игрока'
        ordering = ['year', '-mean']
