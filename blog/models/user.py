from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.models.database import db
from blog.security import flask_bcrypt

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
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    is_staff = Column(Boolean, nullable=False, default=False)
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    _password = Column(LargeBinary, nullable=True)
    #добавляем связь с автором
    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)
    
    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)


