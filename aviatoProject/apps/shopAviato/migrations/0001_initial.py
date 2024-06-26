# Generated by Django 5.0.1 on 2024-02-01 13:05

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(default='', max_length=200, verbose_name='Название категории (РУ)')),
                ('name_az', models.CharField(default='', max_length=200, verbose_name='Название категории (АЗ)')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name_ru', models.CharField(max_length=200, verbose_name='Цвет (РУ)')),
                ('color_name_az', models.CharField(max_length=200, verbose_name='Цвет (АЗ)')),
                ('hex_code', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=1000)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Размер')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.ImageField(upload_to='')),
                ('title_ru', models.CharField(max_length=500, verbose_name='Название товара (РУ)')),
                ('title_az', models.CharField(max_length=500, verbose_name='Название товара (АЗ)')),
                ('price', models.IntegerField()),
                ('short_description_ru', models.CharField(max_length=1500, verbose_name='Краткое описание (РУ)')),
                ('short_description_az', models.CharField(max_length=1500, verbose_name='Краткое описание (АЗ)')),
                ('full_description_ru', ckeditor.fields.RichTextField(verbose_name='Полное описание (РУ)')),
                ('full_description_az', ckeditor.fields.RichTextField(verbose_name='Полное описание (АЗ)')),
                ('trading', models.BooleanField(default=False, verbose_name='В тренде')),
                ('sale', models.FloatField(default=0.0, verbose_name='Скидка')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopAviato.category', verbose_name='Категория')),
                ('color', models.ManyToManyField(to='shopAviato.color')),
                ('photos', models.ManyToManyField(to='shopAviato.photos')),
                ('reviews', models.ManyToManyField(to='shopAviato.review')),
                ('size', models.ManyToManyField(to='shopAviato.size')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
