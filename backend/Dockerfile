# Базовый образ
FROM python:3.11.9-alpine3.19

WORKDIR /app

# Копирование файлов зависимостей
COPY . /app

# Установка poetry и зависимостей проекта
RUN pip install -r requirements.txt
