# Generated by Django 5.0.1 on 2024-02-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAviato', '0004_product_title_en_alter_product_main_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=500, verbose_name='Название товара (АНГЛ)'),
        ),
    ]
