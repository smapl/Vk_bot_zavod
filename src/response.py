import random


def hello():
    list_responses = [
        "Привет",
        "Алоха",
        "Дравье молодой",
        "У аппарата",
        "Бывай",
        "Здравствуй",
        "Здравье",
    ]
    return random.choice(list_responses)


def answer():
    list_responses = [
        "Всё путем",
        "Чики-пуки",
        "Типа окей",
        "Бывало по лучше",
        "Пока здоровый",
    ]
    return random.choice(list_responses)

