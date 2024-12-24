# FastAPI Project Template

## 📚 Описание проекта
Этот проект представляет собой шаблон на **FastAPI**, который демонстрирует организацию структуры проекта. Шаблон можно использовать для старта разработки веб-приложений с использованием FastAPI. Проект нацелен на создание основы для пет проектов.

## 📊 Структура проекта
```
template/
|-- backend/
|   |-- api/
|   |   |-- endpoints/
|   |   |   |-- example.py      # Пример API эндпоинта
|   |   |-- dependencies.py    # Зависимости проекта
|   |   |-- routers.py         # Регистрация маршрутов
|   |-- core/
|   |   |-- config.py          # Конфигурации проекта
|   |-- models/
|   |   |-- models.py          # Определение моделей
|   |-- schemas/
|   |   |-- example.py         # Pydantic схемы
|   |-- services/
|   |   |-- example_service.py # Логика сервисов
|   |-- main.py                # Точка входа в приложение
|-- tests/
|   |-- test_example.py        # Тесты
|-- requirements.txt           # Зависимости проекта
|-- README.md                  # Документация проекта
```

## 🚀 Запуск проекта

1. **Создайте виртуальное окружение и установите зависимости**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Запустите сервер**:

**Для разработки**:
   ```bash
   python3 main.py
   ```
**Для теста локально**:
   ```bash
   docker-compose up --build
   ```


3. **Проверьте работу API**:
   Откройте [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для просмотра автоматической документации Swagger UI.

---

👀 **Автор**: *Артём Жуков*  
👤 **Telegram**: [Art_py](https://t.me/Art_py)

