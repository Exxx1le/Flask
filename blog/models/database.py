from flask_sqlalchemy import SQLAlchemy

#нициализируем объект SQLAlchemy для работы с БД
db = SQLAlchemy()

__all__ = [
    "db",
]
