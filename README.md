# cat-charity-2

## Описание

Веб-сервис благотворительного фонда поддержки котиков реализованного при помощи фреймворка FastAPI. Проект позволяет управлять благотворительными проектами и пожертвованиями через REST API.

Также реализована авторизация пользователей, и упраление ими.

В данном проекте есть два типа сущности:

- Проект пожертвования (CharityProject)
- Пожертвование (Donation)

При создании пожертвования сумма распределяется между открытыми проектами автоматически.

## Ключевые технологии и библиотеки:

- [Python](https://www.python.org/);
- [FastAPI](https://fastapi.tiangolo.com/);
- [SQLAlchemy](https://www.sqlalchemy.org/);
- [Alembic](https://alembic.sqlalchemy.org/en/latest/);
- [Uvicorn](https://uvicorn.dev/);
- [SQLite](https://sqlite.org/).

## Установка и запуск

Клонируйте репозиторий, создайте виртуальное окружение и установите зависимости:

```bash
git clone https://github.com/DeathPolarizer/cat_charity-1.git
cd cat_charity-1
python3 -m venv .venv
. .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

Создайте `.env` файл с переменными окружения:

```bash
touch .env
```

Все необходимые для запуска переменные окружения перечислены в файле `.env-example`.

Мигрируйте базу данных:

```bash
alembic upgrade head
```

Запустите проект:

```bash
uvicorn app.main:app --reload
```

## API

Документаци API endpoints проекта располагается по адресу после запуска приложения [тут](https://127.0.0.1:8000/docs)

## Автор проекта:

Смирнов Дмитрий - [Github](https://github.com/DeathPolarizer/)
