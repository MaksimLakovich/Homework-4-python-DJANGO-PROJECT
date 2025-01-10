from django.contrib import admin
from catalog.models import Category, ContactsData, Product


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


@admin.register(ContactsData)
class ContactsDataAdmin(admin.ModelAdmin):
    """Настройка отображения данных модели ContactsData в админке."""
    list_display = ("country", "tax_id", "address")
