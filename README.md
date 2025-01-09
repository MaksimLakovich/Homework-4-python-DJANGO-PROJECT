# Интернет-магазин "Skystore"


[1. Цель проекта](#title1) / 
[2. Описание HTML-шаблонов](#title2) / 
[3. Контроллеры](#title3) / 
[4. Модели](#title4) / 
[5. Админка](#title5) /
[5. Установка проекта](#title6) / 
[6. Получение ключей](#title7) /


## <a id="title1">1. Цель проекта</a>
Создание проекта Django для интернет-магазина "Skystore".
Интернет-магазина для хранения разнообразных плагинов и примеров кода, который будет продаться.

1. Получить базовые навыки работы с ***Bootstrap***;
2. Получить базовые навыки работы с ***Django***.

    
## <a id="title2">2. Описание HTML-шаблонов для приложения Catalog в `media/html_patterns/`</a>
1. Файл ***media/html_patterns/Home.html***: содержит HTML-шаблон для страницы "Главная", согласно прототипа из ТЗ:
![Прототип для страницы "Главная"](media/html_patterns/Home_page.png)

2. Файл ***media/html_patterns/Contacts.html***: содержит HTML-шаблон для страницы "Контакты", согласно прототипа из ТЗ:
![Прототип для страницы "Контакты"](media/html_patterns/Contacts_page.png)


   
## <a id="title3">3. Описание контроллеров (view) приложения Catalog в `catalog/views.py`</a>

1) Реализация контроллеров в модуле ***catalog/views.py***:
   - Функциональный контроллер `home_page()` - контроллер для отображения домашней страницы (***home.html***):
   Контроллер обрабатывает следующие запросы:
     - **GET-запрос**: контроллер рендерит шаблон home.html
   - Функциональный контроллер `contacts_page()` - контроллер для отображения страницы "Контакты" (***contacts.html***).
   Контроллер обрабатывает следующие запросы:
     - **GET-запрос**: контроллер рендерит шаблон contacts.html;
     - **POST-запрос**: контроллер получает данные из формы (name) и возвращает простой HTTP-ответ об успешности отправки данных.

2) Настроена маршрутизация для данных контроллеров в модуле ***catalog/urls.py***.
В маршрутизации используется пространство имен app_name = CatalogConfig.name = Catalog.



## <a id="title4">4. Описание моделей (models) приложения Catalog в `сatalog/models.py`</a>

1) Реализация модели ***Category***, которая представляет категорию товаров в интернет-магазине:
   - наименование (category_name);
   - описание (description).
2) Реализация модели ***Product***, которая представляет товар в интернет-магазине:
   - наименование (product_name);
   - описание (description);
   - изображение (image);
   - категория (category);
   - цена за покупку (price);
   - дата создания (created_at);
   - дата последнего изменения (updated_at).



## <a id="title5">5. Описание настроек админки (admin) приложения Catalog в `сatalog/admin.py`</a>

1) Для модели *"Category"* в админке настроено отображение данных (***CategoryAdmin***):
   - Отображаемые поля: "id", "category_name";
   - Поля поиска: "category_name", "description".
2) Для модели *"Product"* в админке настроено отображение данных (***ProductAdmin***):
   - Отображаемые поля: "id", "product_name", "price", "category";
   - Поля фильтрации: "category";
   - Поля поиска: "product_name", "description".



## <a id="title6">6. Установка проекта</a>
1. Клонируйте репозиторий:
```
git clone https://github.com/MaksimLakovich/Homework-4-python-DJANGO-PROJECT.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```



## <a id="title7">7. Получение ключей. Описание файла .env.example</a> 
1. Создайте файл .env в корне проекта из копии подготовленного файла `.env.example`, в котором описаны названия всех переменных, необходимых для работы приложения.
2. Замените значения переменных реальными данными.
3. В модуле `settings.py` существует секретный ключ `SECRET_KEY`, который рекомендуется в целях безопасности хранить в тайне:
4. Файл .env должен содержать данные:
   - Настройки секретного ключа проекта:
     - SECRET_KEY_FOR_PROJECT = *secret_key_here*
   - Настройки дебага (обратить внимание, что в settings.py дебаг дополнительно должен быть описан так: DEBUG = True if os.getenv('DEBUG') == 'True' else False):
     - DEBUG = True
   - Настройки БД:
     - DATABASE_SKYSTORE = *write_here*
     - DATABASE_USER = *write_here*
     - DATABASE_PASSWORD = *write_here*
     - DATABASE_HOST = *write_here*
     - DATABASE_PORT = *write_here*
