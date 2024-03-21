# Generated by Django 5.0.1 on 2024-03-06 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAviato', '0011_order_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchuase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=2000)),
                ('address', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='PurchuaseQuntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopAviato.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='purchuase',
            name='products',
            field=models.ManyToManyField(blank=True, to='shopAviato.purchuasequntity'),
        ),
    ]