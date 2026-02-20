# Effective Mobile — Тестовое задание DevOps

Простое веб-приложение: Python HTTP-сервер за Nginx reverse proxy, запущенные в Docker-контейнерах.

## Структура проекта

```
.
├── backend/
│   ├── Dockerfile          # Сборка образа backend
│   └── app.py              # Python HTTP-сервер
├── nginx/
│   └── nginx.conf          # Конфигурация Nginx reverse proxy
├── docker-compose.yml      # Оркестрация сервисов
├── .env.example            # Шаблон переменных окружения
└── README.md
```

## Архитектура

```
Клиент (HTTP)
    │
    ▼
┌──────────┐        ┌──────────┐
│  Nginx   │───────▶│ Backend  │
│ :80      │  proxy │ :8080    │
│(публичный)│       │(внутренн.)│
└──────────┘        └──────────┘
     app-network (bridge)
```

- **Nginx** принимает HTTP-запросы на порт 80 и проксирует их на backend-сервис.
- **Backend** — Python `http.server`, отвечает текстом `Hello from Effective Mobile!` на `/`.
- Backend **не доступен** с хоста — работает только внутри Docker-сети.

## Запуск

### Требования

- Docker
- Docker Compose

### Старт

```bash
docker compose up -d --build
```

### Проверка

```bash
curl http://localhost
```

Ожидаемый ответ:

```
Hello from Effective Mobile!
```

### Остановка

```bash
docker compose down
```

## Конфигурация

Переменные окружения задаются через файл `.env` (см. `.env.example`):

| Переменная             | По умолчанию       | Описание                          |
|------------------------|---------------------|-----------------------------------|
| `COMPOSE_PROJECT_NAME` | `effective-mobile`  | Имя проекта Docker Compose        |
| `APP_PORT`             | `8080`              | Порт backend-приложения           |
| `NGINX_PORT`           | `80`                | Публикуемый порт Nginx на хосте   |

## Технологии

- Python 3.12 (alpine)
- Nginx 1.27 (alpine)
- Docker / Docker Compose
