# WhatsApp Reminder

Это приложение для создания напоминаний через WhatsApp. Пользователи отправляют сообщения в формате "Напомни в YYYY-MM-DD HH:MM текст", и приложение сохраняет напоминание, а затем отправляет его в указанное время.

## Что оно делает?
- Принимает команды через WhatsApp с помощью GreenAPI.
- Сохраняет напоминания в базе данных PostgreSQL.
- Отправляет уведомления в заданное время через Celery.

## Технологии

- **Django**
- **GreenAPI**
- **Celery**
- **Redis**
- **PostgreSQL**
- **Docker**
- **ngrok**
- **nginx**

## Предварительные требования

- Python 3.10
- Docker и Docker Compose
- Аккаунт GreenAPI ([green-api.com](https://green-api.com/))
- Redis
- PostgreSQL
- ngrok

1) Склонируйте репозиторий https://github.com/Vlad29012003/WhatsAppReminder.git

2) 2. Настрой окружение .env
  
SECRET_KEY='django-insecure-i5if%5v%9f#cggyv7i@o)@-d36$g^d3&ncjn8$y_w)@2o5zu@2'
DJANGO_SETTINGS_MODULE=core.settings.base
DEBUG=True
POSTGRES_DB=reminder_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

GREEN_API_BASE_URL=https://7105.api.greenapi.com
GREEN_API_ID_INSTANCE=7105196977
GREEN_API_TOKEN_INSTANCE=df0c691ab9e24a4eb65a060e9f04b46313fb402262eb4123bb
GREEN_API_PHONE_NUMBER=996707828028


3. Установите  зависимости
pip install -r requirements.txt

Если с Docker, пропусти этот шаг.

4) Настрой GreenAPI
войдите в green api и создайте инстанс
Укажи вебхук URL: <ngrok_url>/api/reminders/webhook/ (например, https://cfd4-92-62-70-32.ngrok-free.app/api/reminders/webhook/). в зависимости который у вас будет в ngrok

5) Запустить приложение через Docker
6) docker-compose up --build + полезные комманды
7) docker stop $(docker ps -a -q)
8) docker rm -f $(docker ps -aq)
9) docker rmi $(docker images -q)
10) docker-compose up --d
11) docker-compose up --build



Использование
Отправь сообщение в WhatsApp на ваш номер с другого устройства 

ИЗВЕСТНЫЕ ПРОБЛЕММЫ И РЕШЕНИЯ (которые я лично заметил)

Использование Twilio 
При попытке подключить номер Twilio выдавал ошибку:
(Too many attempts, please try again after some time) так каждый час без доступа к платформе 

Использование GrenAPI
Вебхуки застревают
Одно и то же сообщение повторяется в логах.
GreenAPI не удаляет уведомления из очереди.
Решение Геморойное это заново перерегестрироваться и создавать новый инстанс но и в таком случае он будет брать только одно сообщение и только от одного пользователя 

 
Использование WATI 
Проблема с WATI
WATI не поддерживает бесплатный тариф Web hooks  куда можно отправить эндпоинт


Использование Yowsup
так как Yowsup не официальная библеотека ватсап обновил свою защиту поэтому ее использование устарело ( по моему мнению :)
последние большие изменения были больше 2 лет назад

ПРОБЛЕММЫ С ФУНКЦИОНАЛЬНОСТЬЮ 
Бот не полностью выполняет свою задачу из-за ограничений выбранных инструментов:
Многие рассмотренные API (Twilio, WATI, Yowsup) либо не работали с номером, либо были платными, либо устарели.
GreenAPI, хоть и бесплатный, часто "застревает" на вебхуках, что ломает стабильность отправки и обработки сообщений.
В результате напоминания могут не доходить вовремя или вообще не отправляться из-за этих технических ограничений.




мои сильные стороны
Несмотря на проблемы с WhatsApp-инструментами, обратите внимание на следующие достижения проекта:

** Сборка Docker с Nginx и PgBouncer **
Проект полностью контейнеризирован с использованием Docker Compose.
Nginx настроен как обратный прокси для обработки запросов.
PgBouncer добавлен для оптимизации подключений к PostgreSQL, что улучшает производительность базы данных

** Swagger для API: **
Добавлена документация эндпоинтов через Swagger по пути 
(ваш апи)
http://192.168.31.220/api/swagger/

** Тесты: **
Написаны unit-тесты для проверки эндпоинтов и логики обработки сообщений 

Эндпоинт для отправки сообщений:

Реализован эндпоинт /api/reminders/send-message/ (POST), позволяющий отправлять сообщения пользователям через API. Пример:
curl -X POST <ngrok_url>/api/reminders/send-message/ \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "996707828028", "message": "Тестовое сообщение"}'
