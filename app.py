import os

from flask import Flask, request, jsonify

from config import path_in_file
from utils import get_commands, open_files

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data\\")

list_command = ["filter", "map", "unique", "sort", "limit", "regex"]


@app.route('/')
def index():
    return jsonify(open_files(path_in_file))


@app.route("/perform_query")
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    # return app.response_class('', content_type="text/plain")
    cmd1 = request.args.get("cmd1")
    value1 = request.args.get("value1")
    cmd2 = request.args.get("cmd2")
    value2 = request.args.get("value2")
    file_name = request.args.get("file_name")

    if cmd1 not in list_command or cmd2 not in list_command:
        return 'bad request', 400

    res1 = get_commands(cmd1, value1, open_files(DATA_DIR+file_name))
    res2 = get_commands(cmd2, value2, res1)

    return jsonify(res2)


if __name__ == "__main__":
    app.run(debug=True)
