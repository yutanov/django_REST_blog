# django_REST_blog

<h2>Описание</h2>
<br>
Задействованы фреймворки django, django REST framework.
Хранение данных осуществляется в субд PostgreSQL
Проект упакован в контейнер docker-compose
</br>

<br>
Представлен REST API для системы комментариев блога
Возможность добавления статьи и комметариев, в свою очередь к каждому комментарию также может быть добавлен комментарий.
Вложенность комментариев неограничена.
Есть система аутентификации. Superuser - login: admin, password: admin
</br>

<br>
Доступны следующие панели администрирования URLS:

Статьи:
articles/
articles<drf_format_suffix:format>
articles/<int:pk>/
articles/<int:pk><drf_format_suffix:format>

Комментарии:
comments/
comments<drf_format_suffix:format>
comments/<int:pk>/
comments/<int:pk><drf_format_suffix:format>

Пользователи:
users/
users<drf_format_suffix:format>
users/<int:pk>/
users/<int:pk><drf_format_suffix:format>

Админка:
admin/
</br>

<h2>Установка:</h2>

> git clone https://github.com/yutanov/django_REST_blog.git

> cd django_REST_blog

> docker-compose up
