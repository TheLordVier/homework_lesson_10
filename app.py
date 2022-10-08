# Импортируем фреймворк Flask
from flask import Flask
# Импортируем функции из utils_app.py, которые будем использовать
from utils_app import *

# Инициализируем приложение
app = Flask(__name__)


@app.route("/")
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all()
    result: str = format_candidates(candidates)
    return result


@app.route("/candidates/<int:uid>")
def page_candidate(uid):
    """Вывод кандидата по его pk"""
    candidate: dict = get_by_pk(uid)
    result = f'<img src={candidate["picture"]}>'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """Вывод кандидатов, в списке навыков у которых содержится определенный skill (навык)"""
    candidates: list[dict] = get_by_skill(skill)
    result = format_candidates(candidates)
    return result


app.run()
