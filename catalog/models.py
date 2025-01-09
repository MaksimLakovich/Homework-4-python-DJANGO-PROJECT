from django.db import models


class Category(models.Model):
    """Модель Category представляет категорию товаров в интернет-магазине."""
    category_name = models.CharField(max_length=100, verbose_name="Наименование категории", help_text="Введите название категории", unique=True, blank=False)
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории", blank=True)

    def __str__(self):
        """Метод определяет строковое представление объекта. Полезно для отображения объектов в админке/консоли."""
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]
        db_table = "catalog_categories"


class Product(models.Model):
    """Модель Product представляет товар в интернет-магазине."""
    product_name = models.CharField(max_length=100, verbose_name="Наименование товара", help_text="Введите название товара", unique=True, blank=False)
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара", blank=True)
    image = models.ImageField(upload_to='product_photo/', verbose_name='Фотография товара', help_text="Загрузите фото товара", blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products", help_text="Выберите категорию", blank=True)
    price = models.FloatField(help_text="Укажите цену товара", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Метод определяет строковое представление объекта. Полезно для отображения объектов в админке/консоли."""
        return f"{self.product_name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product_name"]
        db_table = "catalog_products"
