from django.db import models
from datetime import datetime
from os.path import splitext


def img_path(instance, filename):
    return 'news/%s_%s%s' % (instance.pk, datetime.now().timestamp(), splitext(filename)[1])


class News(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название новости')
    short_description = models.TextField(max_length=100, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    # background_img = models.ImageField(verbose_name='Заставка', blank=True, null=True, upload_to=img_path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']
