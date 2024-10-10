# FastAPI Auth System with Redis Cache

## Описание проекта

Этот проект представляет собой приложение для аутентификации и авторизации, разработанное с использованием **FastAPI** и **Redis** в качестве кеша. Приложение предоставляет API для регистрации и аутентификации пользователей, а также включает поддержку OAuth 2.0 и JWT (JSON Web Token) для безопасной передачи данных.

### Почему это приложение хорошо подходит для тестирования развертывания?

| Причина                          | Описание                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| **Легкость развертывания**       | Приложение использует Docker, что упрощает развертывание и управление зависимостями.     |
| **Быстрая разработка**           | FastAPI обеспечивает высокую производительность и быструю разработку благодаря документации Swagger. |
| **Эффективное управление сессиями** | Использование Redis в качестве кеша позволяет быстро управлять сессиями пользователей.    |
| **Безопасность**                 | Реализует аутентификацию и авторизацию с использованием современных стандартов безопасности. |
| **Документация API**             | Автоматически сгенерированная документация Swagger упрощает тестирование API.           |

## Установка

### Предварительные требования

- [Docker](https://www.docker.com/get-started) (и Docker Compose)
- Python 3.8 или выше (если вы хотите запускать приложение локально без Docker)

### Запуск через Docker

Следуйте этим шагам, чтобы запустить приложение с помощью Docker:

1. **Склонируйте репозиторий**:

   ```bash
   git clone https://github.com/ваш_логин/имя_репозитория.git
   cd имя_репозитория
Запустите Docker Compose:

docker-compose up --build
Перейдите в браузере по адресу http://localhost:8000, чтобы увидеть приложение в действии.

Для доступа к документации API перейдите по адресу http://localhost:8000/docs.

Использование API
Метод	Эндпоинт	Описание
POST	/register	Регистрация нового пользователя.
POST	/login	Аутентификация и получение токена JWT.
GET	/protected	Доступ к защищённым ресурсам (требует токен).
Вклад
Если вы хотите внести свой вклад в проект, создайте новый репозиторий или сделайте форк этого проекта и создайте Pull Request.

Лицензия
Этот проект лицензирован под MIT License - смотрите файл LICENSE для подробностей.

### Как добавить `README.md` в ваш репозиторий

1. Создайте новый файл с именем `README.md` в корневом каталоге вашего проекта.
2. Скопируйте и вставьте обновлённый текст в файл.
3. Сохраните изменения.
4. Добавьте файл в Git:

   ```bash
   git add README.md
Сделайте коммит:


git commit -m "Добавлен README.md"
Отправьте изменения на удалённый репозиторий:

git push origin master
