# Abebe Gashe Portfolio

A professional developer portfolio for Abebe Gashe, built with a React frontend and a Django REST backend.

## Overview

This project presents a modern, responsive portfolio for a recent Computer Science graduate interested in backend development, full-stack product engineering, databases, and AI-assisted applications. The website includes a homepage, about section, skills overview, featured project, certificates, and contact section.

## Features

- Responsive dark-themed portfolio design
- Section-based navigation
- Skills grouped by programming language, frontend, backend, database, and tools
- Featured project card for the Skill-Based Employment Platform
- Certificate cards with issue information
- Contact section and demo contact form UI
- Django REST API for health checks and project data
- Frontend fallback behavior when the backend is unavailable

## Technology stack

Frontend:
- React
- Vite
- JavaScript
- CSS modules/custom styling

Backend:
- Python
- Django
- Django REST Framework
- SQLite for local development
- PostgreSQL-ready configuration for production

## Project structure

```text
my-developer/
├── .venv/
├── backend/
│   ├── config/
│   ├── portfolio/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   └── db.sqlite3 (generated locally)
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── .env.example
│   └── vite.config.js
├── .gitignore
├── README.md
└── package-lock.json (optional if using root scripts)
```

## Prerequisites

- Node.js 18+
- Python 3.12+
- npm
- A terminal such as VS Code integrated terminal

## Frontend setup

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

The frontend uses `VITE_API_URL` to connect to Django. For local development the default is `http://127.0.0.1:8000`.

## Backend setup

```bash
cd my-developer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install Django djangorestframework django-cors-headers psycopg2-binary python-dotenv
cd backend
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Environment variables

### Frontend

```env
VITE_API_URL=http://127.0.0.1:8000
```

### Backendr

```env
DJANGO_SECRET_KEY=replace-with-a-secure-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
FRONTEND_URL=http://127.0.0.1:5173
```

## API endpoints

- `GET /api/health/` returns a simple health response.
- `GET /api/projects/` returns the project list used by the frontend.
- Opening the backend root URL redirects to the frontend URL configured by `FRONTEND_URL`.

## How to run both services

Open two terminals:

Terminal 1 (backend):
```bash
cd my-developer/backend
. ..\.venv\Scripts\Activate.ps1
python manage.py runserver
```

Terminal 2 (frontend):
```bash
cd my-developer/frontend
npm run dev -- --host 0.0.0.0
```

## Free deployment (Render + Vercel)

The repository includes a Render Blueprint at `render.yaml` for the Django API. Deploy the backend first, then the Vite frontend:

1. Push the repository to GitHub.
2. In Render, create a new **Blueprint** and select this repository. Apply the `my-developer-api` service defined in `render.yaml`. Render generates `DJANGO_SECRET_KEY` and runs database migrations when the service starts.
3. Copy the backend URL (for example, `https://my-developer-api.onrender.com`). In the Render service's environment settings, set `CORS_ALLOWED_ORIGINS`, `CSRF_TRUSTED_ORIGINS`, and `FRONTEND_URL` to the Vercel site origin. You can enter a temporary placeholder initially and update it after deploying the frontend.
4. In Vercel, import this GitHub repository and set **Root Directory** to `frontend`. Vercel detects Vite; set the environment variable `VITE_API_URL` to the Render backend URL, without a trailing slash, then deploy.
5. Copy the Vercel production origin (for example, `https://my-developer.vercel.app`) into the three Render variables from step 3, then redeploy the backend.
6. Verify `https://<your-render-service>.onrender.com/api/health/` returns a JSON response with `"status": "ok"`.

For live contact email delivery, configure `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, and `EMAIL_TO` in Render. Do not put real credentials in the repository. Without working SMTP credentials, the API will report that email delivery is unavailable.

Render's free web service can sleep when idle, so its first request after inactivity may be slow. The current SQLite database is suitable for this simple deployment, but Render's free instance filesystem is ephemeral: saved contact submissions can be lost when the service restarts or is redeployed. Use a persistent PostgreSQL database if you need contact submissions retained.

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Initial portfolio implementation"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```

## Notes

- Do not commit real secrets or production credentials.
- The contact form is a UI placeholder and should be connected to an email provider or backend endpoint when production-ready.
- The project data is intentionally easy to modify from a single source file.
