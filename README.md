# Установка
1) Убедитесь, что у вас установлен poetry
2) Создайте виртуальное окружение:
```bash
poetry config virtualenvs.in-projects true

# для установки со всеми зависимостями (для бота, разработки, тестов)
poetry install

# без установки зависимостей для разработки
poetry install -without dev

# без установки зависимостей для тестов
poetry install -without test

# для установки только зависимостей бота
poetry install --only-root
```
3) Активируйте окружение:
```bash
poetry shell
```
4) Запустите бота:
```bash
python s21_bot/main.py
```

При разработке не забудте повесить пре-коммит хуки:
```bash
pre-commit install
```
