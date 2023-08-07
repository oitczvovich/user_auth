# Application user_auth

## Description

Test Task: Building a User Management System

A user management system in the form of a web application. 
Using RESTful API endpoints, functions for user registration, login, retrieve user profile, update user profile and delete account are implemented.

Configured automatic creation of the first superuser at project startup.

## Ключевые технологии и библиотеки:
- [Python](https://www.python.org/); 3.11
- [FastAPI](https://fastapi.tiangolo.com/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);
- [Alembic](https://pypi.org/project/alembic/);
- [Pydantic](https://pypi.org/project/pydantic/);

## Установка
1. Clone the repository:
```
https://github.com/oitczvovich/user_auth
```
2. Activate venv and install dependencies, Python version required:
```
python -m venv venv

Windows:
source venv/Scripts/activate
Linux:
. venv/bin/activate

python -m pip install -U pip
pip install -r requirements.txt
```
3. Create an .env file in the root directory with the following contents:
```
APP_TITLE=Name app
APP_DESCRIPTION=APP_DESCRIPTION
DATABASE_URL='sqlite+aiosqlite:///./fastapi.db'
SECRET=<secret>
FIRST_SUPERUSER_EMAIL=<email superuser>
FIRST_SUPERUSER_PASSWORD=<password superuser>
FIRST_NAME=<FIRST_NAME_ADMIN>

```
4. Apply migrations to create a SQLite database if required:
```
alembic init --template async alembic
alembic revision --autogenerate -m "First migration"
alembic upgrade head
```
5. The project is ready to be launched.

To run the project locally, execute the command:
```
uvicorn user_auth.main:app --reload
```
The service will be launched and available at the following addresses:
- http://127.0.0.1:8000 - API
- http://127.0.0.1:8000/docs - automatically generated Swagger documentation

### Autor
Vladimir Skalatskiy
https://github.com/oitczvovich

