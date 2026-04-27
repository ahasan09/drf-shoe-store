# Improvement Plan: drf_shoestore

## Overview
Django REST Framework shoe store API with 4 endpoints. No authentication, no tests, no API documentation, and no containerization.

## Improvements

### Security (High Priority)
- Add authentication and authorization — currently all endpoints appear to be publicly writable
- Use JWT authentication (`djangorestframework-simplejwt`) for token-based auth
- Add Django's `ALLOWED_HOSTS` and `SECRET_KEY` configuration via environment variables (not hardcoded)
- Add CORS configuration (`django-cors-headers`)

### Testing
- Add pytest + `pytest-django` unit tests for all 4 endpoints (test CRUD operations, validation, and auth)
- Add factory_boy for test data generation
- Target ≥80% code coverage
- Add GitHub Actions CI to run tests on every PR

### API Documentation
- Add `drf-spectacular` to auto-generate OpenAPI 3.0 schema
- Expose Swagger UI at `/api/schema/swagger-ui/` and ReDoc at `/api/schema/redoc/`

### Code Quality
- Add input validation using DRF serializer validators (min/max price, required fields)
- Add proper error responses with consistent JSON structure
- Use `django-environ` or `python-decouple` for environment variable management
- Add `black` + `ruff` for formatting and linting

### DevOps
- Add a `Dockerfile` and `docker-compose.yml` for local development (app + PostgreSQL)
- Switch from SQLite to PostgreSQL for production parity
- Add a GitHub Actions CI pipeline: lint + test + build Docker image
