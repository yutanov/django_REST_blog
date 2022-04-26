# django_REST_blog

<h2>Описание</h2>

<br>Задействованы фреймворки django, django REST framework.</br>
<br>Хранение данных осуществляется в субд PostgreSQL</br>
<br>Проект упакован в контейнер docker-compose</br>

<br>Представлен REST API для системы комментариев блога</br>
<br>Возможность добавления статьи и комметариев, в свою очередь к каждому комментарию также может быть добавлен комментарий.</br>
<br>Вложенность комментариев неограничена.</br>
<br>Есть система аутентификации. Superuser - login: admin, password: admin</br>

<br>Доступны следующие панели администрирования URLS:</br>

<br>Статьи: </br>
<br>articles/ </br>
<br>articles<drf_format_suffix:format> </br>
<br>articles/<int:pk>/ </br>
<br>articles/<int:pk><drf_format_suffix:format> </br>

<br>Комментарии: </br>
<br>comments/ </br>
<br>comments<drf_format_suffix:format> </br>
<br>comments/<int:pk>/ </br>
<br>comments/<int:pk><drf_format_suffix:format> </br>

<br>Пользователи: </br>
<br>users/ </br>
<br>users<drf_format_suffix:format> </br>
<br>users/<int:pk>/ </br>
<br>users/<int:pk><drf_format_suffix:format> </br>

<br>Админка: </br>
<br>admin/ </br>

<h2>Установка:</h2>

> git clone https://github.com/yutanov/django_REST_blog.git

> cd django_REST_blog

> docker-compose up
