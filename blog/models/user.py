from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from flask_login import UserMixin

"""
UserMixin имеет метод is_authenticated(), который возвращает True, если пользователь предоставил
действительные учетные данные;
● имеет метод is_active(), который возвращает True, если учетная запись пользователя активна;
● имеет метод is_anonymous(), который возвращает True, если текущий пользователь является
анонимным пользователем;
● имеет метод get_id(), который, учитывая пользовательский экземпляр, возвращает уникальный
ID для этого объекта.
"""

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    email = Column(String(255), nullable=False, default="", server_default="")
    
    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"


