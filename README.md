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
```

## API endpoints

- `GET /api/health/` returns a simple health response.
- `GET /api/projects/` returns the project list used by the frontend.

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

## Deployment guidance

### Django backend

Use a production host such as Render, Railway, or a VPS. Set environment variables for the secret key, allowed hosts, and database configuration. Use PostgreSQL for production instead of the local SQLite database.

### React frontend

Deploy the static frontend to Vercel, Netlify, or Cloudflare Pages. Point `VITE_API_URL` to the live Django backend domain after deployment.

### PostgreSQL database

For production, configure a PostgreSQL service and set database variables in the backend environment. Example fields include database name, username, password, and hostname.

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
