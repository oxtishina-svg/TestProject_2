# Учебный проект обработки банковских операций

## Описание

Проект содержит функции для обработки информации о банковских картах, счетах и операциях.

Реализованы функции:
- маскировки номера банковской карты;
- маскировки номера банковского счета;
- определения типа платежного инструмента и его маскировки;
- преобразования даты к удобному формату;
- фильтрации списка операций по статусу;
- сортировки операций по дате.

## Структура проекта

```text
src/
    masks.py
    widget.py
    processing.py
tests/
    test_masks.py
    test_widget.py
    test_processing.py
```

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/oxtishina-svg/TestProject_2.git
```

2. Перейдите в папку проекта:

```bash
cd TestProject_2
```

3. Установите зависимости:

```bash
poetry install
```

## Использование

### Маскировка карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
```

### Маскировка счета

```python
from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))
```

### Обработка информации о карте или счете

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
```

### Форматирование даты

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
```

### Фильтрация операций

```python
from src.processing import filter_by_state

operations = [
    {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
    {"state": "CANCELED", "date": "2024-02-10T12:00:00.000000"},
]

result = filter_by_state(operations)
```

### Сортировка операций

```python
from src.processing import sort_by_date

operations = [
    {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
    {"state": "CANCELED", "date": "2024-02-10T12:00:00.000000"},
]

result = sort_by_date(operations)
```

## Тестирование

Для тестирования проекта используется библиотека `pytest`.

Тесты расположены в директории `tests` и разделены по модулям проекта:

```text
tests/
    test_masks.py
    test_widget.py
    test_processing.py
```

Для запуска всех тестов выполните:

```bash
pytest
```

В тестах используются фикстуры и параметризация для проверки различных вариантов входных данных.

Для проверки покрытия функционального кода тестами выполните:

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

HTML-отчет о покрытии тестами создается в директории:

```text
htmlcov/
```

Для просмотра отчета откройте файл:

```text
htmlcov/index.html
```

## Автор

Оксана Тишина
