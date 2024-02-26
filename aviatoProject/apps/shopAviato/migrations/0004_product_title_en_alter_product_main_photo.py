# Generated by Django 5.0.1 on 2024-02-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAviato', '0003_alter_product_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(default='English Title', max_length=500, verbose_name='Название товара (АНГЛ)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
