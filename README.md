# ZeroCoder: Учебный Django-проект

ZeroCoder — это учебное Django-приложение, демонстрирующее базовую структуру и работу с несколькими приложениями, маршрутизацией и шаблонами.

## ⚙️ Возможности
- Отдельные Django-приложения: `main`, `data_app`
- Несколько веб-страниц:
  - `/` — главная страница
  - `/new_post/`, `/new` — вспомогательные страницы
  - `/data/`, `/test/` — страницы второго приложения
- Использование HTML-шаблонов с оформлением
- SQLite в качестве базы данных по умолчанию

## 🚀 Запуск проекта
1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
2. Запустите сервер:
    ```bash
    python manage.py runserver
    ```
3. Перейдите в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Структура
```
ZeroCoder/
├── main/         # Главное приложение
├── data_app/     # Дополнительные страницы
├── ZeroCoder/    # Конфигурация проекта
├── templates/    # HTML-шаблоны
├── manage.py     # Управление Django
```

---

Проект создан для обучения и экспериментов с Django.💻