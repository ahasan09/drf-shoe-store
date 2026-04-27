# DRF Shoe Store

Django REST Framework shoe store API with 4 REST endpoints, managed with Poetry.

## Tech Stack
- Python 3
- Django 3
- Django REST Framework
- Poetry (dependency management)

## Project Structure
```
drf_shoestore/
├── api/
│   ├── models.py
│   ├── serializer.py
│   └── views.py
├── manage.py
└── pyproject.toml
```

## Development
```bash
# Install dependencies
poetry install

# Apply migrations
poetry run python manage.py migrate

# Run development server
poetry run python manage.py runserver
```

## Key Notes
- 4 REST endpoints for shoe store resources.
- Uses Poetry for dependency and virtual environment management.
