# Playwright + Pytest + CI example

Этот проект демонстрирует внедрение e2e автотестов на Playwright с использованием Page Object и запуском в CI (GitHub Actions).

## Что реализовано

- Page Object архитектура
- e2e сценарии (login → cart → checkout)
- Параметризация тестов
- Pytest fixtures
- Автоматический запуск тестов в CI при каждом push

## Стек

- Python
- Playwright
- Pytest
- GitHub Actions

## Как запустить локально

```bash
pip install pytest playwright pytest-html
playwright install
pytest
