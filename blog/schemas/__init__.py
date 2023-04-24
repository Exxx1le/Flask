#в этот файл добавляются все схемы из модуля
from blog.api.user import UserList, UserDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.article import ArticleList, ArticleDetail
from blog.schemas.tag import TagSchema
from blog.schemas.user import UserSchema
from blog.schemas.author import AuthorSchema
from blog.schemas.article import ArticleSchema


__all__ = [
    "TagSchema",
    "UserSchema",
    "AuthorSchema",
    "ArticleSchema",
]