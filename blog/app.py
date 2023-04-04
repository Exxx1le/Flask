from flask import Flask
from flask import request
from flask import g
from datetime import time

#создаем экземпляр приложения
app = Flask(__name__)

#регистрируем на путь "/" выполнение функции
@app.route('/', methods=['GET', 'POST'])
def index():
    # name = request.args.get('name', None) - получение данных из query параметров запроса
    return 'Hello!' 
    #можно в return указать код ответа, который выдаст сервер
    #можно также использовать метод Responce()

#обрабатываем слова после / в запросе
#@app.route('/<city>') # можно написать '/<int:city>' или '/<string:city>', чтобы не принимать иное
#def index(city: str):
#   return f'Hello, {city}'

#можно использовать request.method для маршрутизации типов запросов

@app.before_request
def process_before_request():
    """
    запись времени запроса в глобальную переменную g
    """
    g.start_time = time()


@app.after_request
def process_after_request(response):
    """
    добавление времени выполнения запроса в заголовок
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time

    return response

#обработка ошибок 
@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return 'Такой страницы не существует'
