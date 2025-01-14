from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import ContactsData, Product


def home_page(request):
    """Контроллер для отображения домашней страницы (home.html).
    Для отладки контроллер главной/домашней страницы выводит в консоль последние 5 созданных продуктов."""
    # Выборка последних 5 продуктов. Символ '-' перед 'created_at' устанавливает порядок от новых к старым.
    # Если не использовать символ '-' перед 'created_at', то порядок будет наоборот от старых к новым.
    latest_products = Product.objects.order_by("-created_at")[:5]
    # Вывод в консоль данных для отладки
    for product in latest_products:
        print(f"Название: {product.product_name}, Дата создания: {product.created_at}")

    return render(request, "catalog/home.html")


def contacts_page(request):
    """Контроллер для отображения страницы с контактной информацией (contacts.html)."""
    if request.method == "POST":
        name = request.POST.get("name")
        # Если метод запроса POST, контроллер получает данные из формы (name) и возвращает простой HTTP-ответ.
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение успешно отправлено")
    # Если метод запроса — GET, контроллер рендерит шаблон contacts.html
    # Сразу получаю контактные данные из БД, чтоб потом их использовать при рендере шаблона страницы-html
    contacts_data = ContactsData.objects.all()
    return render(request, "catalog/contacts.html", {"contacts_data": contacts_data})
