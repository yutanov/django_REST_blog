# django_REST_blog

<h2>Описание</h2>

<p>Задействованы фреймворки django, django REST framework
  
Хранение данных осуществляется в субд PostgreSQL
  
Проект упакован в контейнер docker-compose</p>

<p>Представлен REST API для системы комментариев блога
  
Возможность добавления статьи и комметариев, в свою очередь к каждому комментарию также может быть добавлен комментарий
  
Вложенность комментариев не ограничена
  
Есть система аутентификации. Для добавления, изменения или удаления статьи или комментария необходима авторизация</p>

<h2>Установка</h2>

Склонируйте репозиторий
> git clone https://github.com/yutanov/django_REST_blog.git

Перейдите в каталог репозитория
> cd django_REST_blog

Создайте образ контейнера
> docker-compose build

Запустите миграции
> docker-compose run web python manage.py migrate

Создайте суперюзера
> docker-compose run web python manage.py createsuperuser

Запустите контейнер
> docker-compose up

Перейдите по адресу http://0.0.0.0:8000/

<h2>Доступны следующие панели администрирования URLS </h2>

<br>Статьи: </br>

> articles/
> 
> articles<drf_format_suffix:format>
> 
> articles/<int:pk>
> 
> articles/<int:pk><drf_format_suffix:format>

<br>Комментарии: </br>

> comments
> 
> comments<drf_format_suffix:format>
> 
> comments/<int:pk>
> 
> comments/<int:pk><drf_format_suffix:format>

<br>Пользователи: </br>

> users
> 
> users<drf_format_suffix:format>
> 
> users/<int:pk>
> 
> users/<int:pk><drf_format_suffix:format>

<br>Админка: </br>

> admin
