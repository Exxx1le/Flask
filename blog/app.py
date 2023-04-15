import os
from datetime import time

from flask import Flask, render_template
from flask import request
from flask import g
from flask_migrate import Migrate

from blog.views.users import users
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
from blog.security import flask_bcrypt
from blog.views.authors import authors_app


#создаем экземпляр приложения
app = Flask(__name__)

# #регистрируем на путь "/" выполнение функции
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # name = request.args.get('name', None) - получение данных из query параметров запроса
#     return 'Hello!' 
#     #можно в return указать код ответа, который выдаст сервер
#     #можно также использовать метод Responce()

# #обрабатываем слова после / в запросе
# #@app.route('/<city>') # можно написать '/<int:city>' или '/<string:city>', чтобы не принимать иное
# #def index(city: str):
# #   return f'Hello, {city}'

# #можно использовать request.method для маршрутизации типов запросов

# @app.before_request
# def process_before_request():
#     """
#     запись времени запроса в глобальную переменную g
#     """
#     g.start_time = time()


# @app.after_request
# def process_after_request(response):
#     """
#     добавление времени выполнения запроса в заголовок
#     """
#     if hasattr(g, "start_time"):
#         response.headers["process-time"] = time() - g.start_time

#     return response

# #обработка ошибок 
# @app.errorhandler(404)
# def handler_404(error):
#     app.logger.error(error)
#     return 'Такой страницы не существует'

#точка входа в приложение
# def create_app() -> Flask:
#     register_blueprints(app)
#     return app

# #подключаем user к приложению
# def register_blueprints(app: Flask):
#     app.register_blueprint(user)

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")

# подключаем БД
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.config["SECRET_KEY"] = "abcdefg123456"
login_manager.init_app(app)

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

migrate = Migrate(app, db, compare_type=True)

#добавляем шифрование
flask_bcrypt.init_app(app)

# не нужно после подключения flask-migrate
# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")


# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
#     from blog.models import User
#     admin = User(username="admin", is_staff=True)
#     james = User(username="james")
    
#     db.session.add(admin)
#     db.session.add(james)
#     db.session.commit()
    
#     print("done! created users:", admin, james)


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    
    db.session.add(admin)
    db.session.commit()
    
    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
    "flask",
    "django",
    "python",
    "sqlalchemy",
    "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")