from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка отображения данных модели Category в админке."""
    list_display = ("id", "category_name",)
    search_fields = ("category_name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройка отображения данных модели Product в админке."""
    list_display = ("id", "product_name", "price", "category",)
    list_filter = ("category",)
    search_fields = ("product_name", "description",)
