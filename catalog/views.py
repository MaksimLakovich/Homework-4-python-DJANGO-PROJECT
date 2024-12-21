from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'catalog/home.html')


def contacts_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Если метод запроса POST, контроллер получает данные из формы (name) и возвращает простой HTTP-ответ.
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение успешно отправлено')
    # Если метод запроса — GET, контроллер рендерит шаблон contacts.html
    return render(request, 'catalog/contacts.html')
