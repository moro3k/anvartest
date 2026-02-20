# Effective Mobile - DevOps Test Assignment

Simple web application: Python HTTP backend behind Nginx reverse proxy, running in Docker containers.

## Project Structure

```
.
├── backend/
│   ├── Dockerfile          # Backend image build instructions
│   └── app.py              # Python HTTP server
├── nginx/
│   └── nginx.conf          # Nginx reverse proxy configuration
├── docker-compose.yml      # Service orchestration
├── .env.example            # Environment variables template
└── README.md
```

## Architecture

```
Client (HTTP)
    │
    ▼
┌──────────┐        ┌──────────┐
│  Nginx   │───────▶│ Backend  │
│ :80      │  proxy │ :8080    │
│ (public) │        │(internal)│
└──────────┘        └──────────┘
     app-network (bridge)
```

- **Nginx** listens on port 80 and proxies all requests to the backend service.
- **Backend** is a Python `http.server` that responds with `Hello from Effective Mobile!` on `/`.
- Backend is **not exposed** to the host — it is accessible only within the Docker network.

## How to Run

### Prerequisites

- Docker
- Docker Compose

### Start

```bash
docker compose up -d --build
```

### Verify

```bash
curl http://localhost
```

Expected response:

```
Hello from Effective Mobile!
```

### Stop

```bash
docker compose down
```

## Configuration

Environment variables can be set via `.env` file (see `.env.example`):

| Variable               | Default            | Description                  |
|------------------------|--------------------|------------------------------|
| `COMPOSE_PROJECT_NAME` | `effective-mobile` | Docker Compose project name  |
| `APP_PORT`             | `8080`             | Backend application port     |
| `NGINX_PORT`           | `80`               | Nginx published port on host |

## Technologies

- Python 3.12 (alpine)
- Nginx 1.27 (alpine)
- Docker / Docker Compose
