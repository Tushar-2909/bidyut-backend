# Bidyut Backend

A Django REST API backend with JWT authentication, custom user roles, admin/user separation, and CORS enabled for frontend integration.

## Tech Stack

- Python 3.10
- Django 5.2
- Django REST Framework 3.16.0
- Simple JWT 5.5.1
- django-cors-headers 4.7.0
- SQLite (current default database)

## Features

- Custom user model with `admin` and `user` roles
- User registration
- JWT login and token refresh
- Authenticated profile endpoint
- Admin-only user listing
- Admin-only user deletion
- Logout using refresh-token blacklist

## Project Structure

```text
bidyut-backend/
|-- backend/
|   |-- manage.py
|   |-- backend/
|   |-- accounts/
|   `-- db.sqlite3
|-- requirements.txt
|-- README.md
`-- .gitignore
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py runserver
```

The API will run at `http://127.0.0.1:8000/`.

## API Endpoints

Base path: `/api/`

- `POST /api/register/` - register a new user
- `POST /api/login/` - obtain access and refresh tokens
- `POST /api/refresh/` - refresh access token
- `GET /api/profile/` - get current authenticated user
- `GET /api/users/` - list users, admin only
- `DELETE /api/delete-user/<id>/` - delete user, admin only
- `POST /api/logout/` - blacklist refresh token

## Sample Request Body

Register:

```json
{
  "email": "user@example.com",
  "username": "demo_user",
  "password": "strongpassword123"
}
```

Login:

```json
{
  "email": "user@example.com",
  "password": "strongpassword123"
}
```

Logout:

```json
{
  "refresh": "your_refresh_token"
}
```

## Deployment Notes

- `requirements.txt` is pinned for reproducible installs.
- The app currently uses SQLite via [backend/backend/settings.py](/d:/6th sem ki padhai/bidyut-backend/backend/backend/settings.py), which is fine for local development but not ideal for production.
- `DEBUG = True` and the hardcoded `SECRET_KEY` should be replaced before deployment.
- `ALLOWED_HOSTS` should be set for your deployed domain.
- `CORS_ALLOW_ALL_ORIGINS = True` is convenient for development, but should be restricted in production.

## Useful Commands

```bash
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py createsuperuser
python backend/manage.py test
```
