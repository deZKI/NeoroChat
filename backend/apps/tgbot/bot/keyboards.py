import random
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рекомендации по рекламе")],
        [KeyboardButton(text="Помощь в коде")],
    ],
    resize_keyboard=True
)


# Функция для генерации случайных слов
def generate_random_queries():
    words = ["Реклама", "Код", "Маркетинг", "Помощь", "Консультация", "Анализ", "Стратегия", "Планирование",
             "Разработка", "Аудит"]
    queries = []

    # Генерируем 3-4 случайные фразы
    for _ in range(3):
        queries.append(random.choice(words))

    return queries


# Функция для создания рандомизированной клавиатуры
def create_randomized_keyboard():
    queries = generate_random_queries()

    # Перемешиваем список фраз
    random.shuffle(queries)

    # Создаем кнопки с этими фразами
    buttons = [[KeyboardButton(text=query)] for query in queries]

    # Создаем клавиатуру
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


# Пример использования клавиатуры
handle_keyboard = create_randomized_keyboard()
