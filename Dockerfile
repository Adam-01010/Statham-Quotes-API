FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое папки app в папку app внутри контейнера
COPY ./app ./app
# Копируем данные
COPY ./data ./data

# 2. Указываем путь к приложению как app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]