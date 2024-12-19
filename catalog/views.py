from django.shortcuts import render



def home_page(request):
    return render(request, 'catalog/home.html')


def contacts_page(request):
    return render(request, 'catalog/contacts.html')


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         # Если метод запроса POST, контроллер получает данные из формы (name и message) и возвращает простой HTTP-ответ.
#         return HttpResponse(f'Спасибо, {name}! Сообщение получено')
#     # Если метод запроса — GET, контроллер рендерит шаблон contact.html
#     return render(request, 'students/contact.html')

