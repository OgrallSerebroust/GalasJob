from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип валюты')

    class Meta:
        verbose_name = 'Тип валюты'
        verbose_name_plural = 'Типы валюты'

    def __str__(self):
        return self.name


class Currency(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Тип валюты")
    name = models.CharField(max_length=128, verbose_name="Имя валюты")
    price = models.PositiveBigIntegerField(verbose_name="Цена валюты")

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class CurrencyImg(models.Model):
    image = models.ImageField(upload_to="static/img", verbose_name="Изображение валюты")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валюта")

    class Meta:
        verbose_name = 'Изображение валюты'
        verbose_name_plural = 'Изображения валюты'

    def __str__(self):
        return f'Изображение валюты - {self.currency}'
