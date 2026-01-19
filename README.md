# MIPT Buisness Club

Этот проект представляет собой платформу для автоматизации процессов Бизнес Клуба МФТИ

## Структура проекта

```bash
project-root/
├─ backend/              # Серверная часть (FastAPI)
│  ├─ app/               # Основной код приложения
│  ├─ alembic/           # Миграции базы данных
│  └─ Dockerfile
├─ frontend/             # Клиентская часть (React + TypeScript)
│  └─ Dockerfile
├─ docker-compose.yml    # Сборка и запуск всех сервисов
├─ .env.example          # Пример файла с переменными окружения
└─ README.md
```

- backend/ — содержит весь серверный код и миграции.
- frontend/ — фронтенд-приложение.
- docker-compose.yml — позволяет поднять все сервисы (бэкенд, фронтенд, база) в одном командном запуске.
- .env.example — пример файла с переменными окружения.

## Настройка .env

Для работы проекта необходимо создать файл .env на основе .env.example и указать свои значения:

```bash
# Сервер
APP_PORT=8000
APP_HOST=0.0.0.0

# Фронтенд
FRONTEND_PORT=8080

# Postgres
POSTGRES_DB=db
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://admin:password@db:5432/db

# Авторизация
SECRET_KEY=secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=30

# Ссылки
REGISTRATION_PAGE_URL="https://mipt.bc/registration/"
```

**Описание переменных:**

- APP_PORT, APP_HOST — порт и хост для бэкенда.
- FRONTEND_PORT — порт для фронтенда.
- POSTGRES\_\* — настройки базы данных.
- DATABASE_URL — URL для подключения к БД и использования Alembic для миграций.
- SECRET_KEY, ALGORITHM — настройки для хеширования и токенов.
- ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS — время жизни токенов.
- REGISTRATION_PAGE_URL — ссылка на страницу регистрации (для фронтенда).

## Запуск на локальном сервере / развертка

1. Склонировать репозиторий:

```bash
git clone https://github.com/Smoooky/mipt_bc.git
cd project-root
```

2. Создать файл **.env** на основе **.env.example** и заполнить нужные значения.
3. Запустить все сервисы через Docker Compose:

```bash
docker compose up --build
```

После этого проект начинает свою работу
