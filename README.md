# Итоговая работа: Selenium + Docker + OpenCart

Проект содержит 11 UI-автотестов для локального сайта OpenCart, который поднимается через Docker Compose. 

## Отличия локального стенда

Для отдельного запуска используется другое имя Docker Compose-проекта и другие порты, поэтому его можно запускать параллельно с другим учебным вариантом:

- OpenCart: `http://localhost:8082`;
- phpMyAdmin: `http://localhost:8889`;
- Docker Compose project name: `work`.

## Структура репозитория

```text
work/
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── TEST_PLAN.md
├── README.md
├── .env.example
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_page.py
│   ├── product_page.py
│   ├── contact_page.py
│   └── account_page.py
├── tests/
│   ├── conftest.py
│   └── test_opencart_ui.py
├── artifacts/
│   └── screenshots/
└── docs/
    └── Отчет.docx
```

## Что проверяют автотесты

В проекте реализовано **11 автотестов**. Проверяются главная страница, поиск, карточка товара, изменение количества, добавление товара в корзину, доступность корзины, форма контактов и форма регистрации.

## 1. Запуск OpenCart через Docker

Перед запуском нужно установить Docker Desktop и дождаться статуса **Engine running**.

В корне проекта уже находится файл `.env`. При необходимости его можно восстановить по `.env.example`:

```env
OPENCART_PORT=8082
PHPADMIN_PORT=8889
OPENCART_HTTPS_PORT=8444
LOCAL_IP=localhost
BASE_URL=http://localhost:8082
HEADLESS=true
```

Запуск контейнеров:

```powershell
docker compose up -d
```

Проверка контейнеров:

```powershell
docker compose ps
```

phpMyAdmin открывается по адресу:

```
http://localhost:8889
```

## 2. Установка зависимостей для тестов

Рекомендуется Python 3.10 или новее.

### Windows PowerShell

```powershell
python -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

## 3. Запуск тестов

Обычный запуск:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -v
```

Запуск с открытым браузером:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -v --headed
```

## 4. Allure-отчет

Создание Allure-результатов:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest --alluredir=allure-results
```

Просмотр отчета:

```powershell
allure serve allure-results
```

## 5. Скриншоты

При падении теста скриншот автоматически сохраняется в папку:

```
artifacts/screenshots/
```