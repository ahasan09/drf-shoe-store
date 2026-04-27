# DRF Shoe Store

A Django REST Framework (DRF) API for a shoe store. Provides endpoints for managing shoes, shoe types, colors, and manufacturers.

## Features

- RESTful API for shoes inventory
- Filter by shoe type, color, and manufacturer
- Browsable API via DRF's built-in UI
- Database seeding via management command

## Tech Stack

- Python 3.8+
- Django 3.x
- Django REST Framework
- SQLite (default database)
- [Poetry](https://python-poetry.org/) — dependency management

## Prerequisites

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/): `pip install poetry`

## Getting Started

### 1. Install dependencies

```bash
git clone https://github.com/ahasan09/drf-shoe-store
cd drf-shoe-store
poetry install
```

### 2. Apply migrations

```bash
poetry run python manage.py makemigrations api
poetry run python manage.py migrate
```

### 3. Seed sample data

```bash
poetry run python manage.py bootstrap_data
```

### 4. Run the server

```bash
poetry run python manage.py runserver
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/shoe/` | List all shoes |
| `POST /api/shoe/` | Create a shoe |
| `GET /api/shoe/{id}/` | Get a shoe by ID |
| `PUT /api/shoe/{id}/` | Update a shoe |
| `DELETE /api/shoe/{id}/` | Delete a shoe |
| `GET /api/shoe_type/` | List shoe types |
| `GET /api/shoe_color/` | List shoe colors |
| `GET /api/manufacturer/` | List manufacturers |

Browse the API at [http://127.0.0.1:8000/api/shoe/](http://127.0.0.1:8000/api/shoe/).

## Alternative: pip install

```bash
pip install django djangorestframework
python manage.py makemigrations api
python manage.py migrate
python manage.py bootstrap_data
python manage.py runserver
```

## Project Structure

```
drf-shoe-store/
├── api/             # App — models, serializers, views, URLs
├── drf_shoestore/   # Project settings and URL config
├── manage.py
└── pyproject.toml   # Poetry dependencies
```
