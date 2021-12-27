from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name