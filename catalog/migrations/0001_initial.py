# Generated by Django 5.1.4 on 2025-01-09 11:19

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
                ('category_name', models.CharField(help_text='Введите название категории', max_length=100, unique=True, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'catalog_categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Введите название товара', max_length=100, unique=True, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, help_text='Введите описание товара', verbose_name='Описание товара')),
                ('image', models.ImageField(help_text='Загрузите фото товара', null=True, upload_to='product_photo/', verbose_name='Фотография товара')),
                ('price', models.IntegerField(help_text='Укажите цену товара')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(help_text='Выберите категорию', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'catalog_products',
                'ordering': ['product_name'],
            },
        ),
    ]
