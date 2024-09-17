# Django приложение для ведения списка продуктов
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
## Описание
Приложение для добавления продуктов в БД и получения их списка. 
## Основные особенности
- API для работы с продуктами (создание и получение списка);
- Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.

## Стек использованных технологий
+ Python 3.11
+ Django 3.2
+ DRF
+ HTML
+ JavaScript

## Запуск проекта
1. Клонируйте репозиторий на вашем локальном компьютере:

```
   git clone https://github.com/nepa27/product_api
   cd product_api
```
   
2. Установите и активируйте виртуальное окружение c учетом версии Python 3.11:
* Если у вас Linux/macOS

```
    python3 -m venv env
    source env/bin/activate
```

* Если у вас Windows

```
    python -m venv venv
    source venv/Scripts/activate
```

+ Обновите менеджер пакетов pip:

```
python -m pip install --upgrade pip
```

+ Затем установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

+ Переходим в репозиторий с manage.py и выполняем миграции:

```
python manage.py migrate
```
3. Запускаем проект:

```
python manage.py runserver
```

Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000,
чтобы взаимодействовать со стартовой страницей приложения.

### API запросы 
* Получение списка продуктов: 
```
http://127.0.0.1:8000/api/products/
```
* Создание нового продукта: 
```
http://127.0.0.1:8000/api/products/create/
```
## Автор

+ [Александр Непочатых](https://github.com/nepa27) 
