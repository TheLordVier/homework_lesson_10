# Импортируем стандартный модуль json
import json


def load_candidates() -> list[dict]:
    """
    Создаём функцию чтения json файла
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all() -> list[dict]:
    """
    Создаём функцию, которая покажет всех кандидатов
    """
    return load_candidates()


def format_candidates(candidates: list[dict]) -> str:
    """
    Создаём функцию форматирования списка кандидатов
    """
    result = "<pre>"
    for candidate in candidates:
        result += f"""
        {candidate["name"]}\n
        {candidate["position"]}\n
        {candidate["skills"]}\n       
        """
    result += "<pre>"
    return result


def get_by_pk(uid: int) -> dict | None:
    """
     Создаём функцию получения кандидата по его pk
     """
    candidates = get_all()
    for candidate in candidates:
        if str(uid) == str(candidate["pk"]):
            return candidate
    return None


def get_by_skill(skill: str) -> list[dict]:
    """
     Создаём функцию которая вернёт кандидатов по навыку
     """
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
