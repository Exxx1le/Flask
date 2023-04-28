from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from blog.schemas import AuthorSchema
from blog.models.database import db
from blog.models import Author, Article


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }

# создать RPC (event), связанный с конкретной моделью — в данном случае мы
# хотим узнать количество статей, связанных с выбранным автором. В таком случае мы добавляем
# новый event, связанный с details resource (с классом AuthorDetail через атрибут events).
class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }