# models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Category(models.Model):
    name_ru = models.CharField(max_length=200, verbose_name='Название категории (РУ)', default='')
    name_az = models.CharField(max_length=200, verbose_name='Название категории (АЗ)', default='')

    def __str__(self):
        return self.name_ru


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='Размер')

    def __str__(self):
        return self.name


class Color(models.Model):
    color_name_ru = models.CharField(max_length=200, verbose_name='Цвет (РУ)')
    color_name_az = models.CharField(max_length=200, verbose_name='Цвет (АЗ)')
    hex_code = models.CharField(max_length=17)

    def __str__(self):
        return self.color_name_ru


class Review(models.Model):
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now=True)


class Photos(models.Model):
    photo = models.ImageField()


class Product(models.Model):
    main_photo = models.ImageField(upload_to='photos')
    photos = models.ManyToManyField(Photos)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products',
                                 default='')

    title_ru = models.CharField(max_length=500, verbose_name='Название товара (РУ)')
    title_az = models.CharField(max_length=500, verbose_name='Название товара (АЗ)')

    price = models.IntegerField()

    short_description_ru = models.CharField(max_length=1500, verbose_name='Краткое описание (РУ)')
    short_description_az = models.CharField(max_length=1500, verbose_name='Краткое описание (АЗ)')
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)

    full_description_ru = RichTextField(verbose_name='Полное описание (РУ)')
    full_description_az = RichTextField(verbose_name='Полное описание (АЗ)')
    reviews = models.ManyToManyField(Review)

    trending = models.BooleanField(default=False, verbose_name='В тренде')
    sale = models.FloatField(default=0.0, verbose_name='Скидка')

    class Meta:
        verbose_name_plural = 'Товары'

