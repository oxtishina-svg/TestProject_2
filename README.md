# Учебный проект обработки банковских операций

## Описание

Проект содержит функции для обработки информации о банковских картах, счетах и финансовых операциях.

Реализованы функции:
- маскировки номера банковской карты;
- маскировки номера банковского счета;
- определения типа платежного инструмента и его маскировки;
- преобразования даты к удобному формату;
- фильтрации списка операций по статусу;
- сортировки операций по дате;
- фильтрации транзакций по валюте с использованием генератора;
- последовательного получения описаний транзакций;
- генерации номеров банковских карт в заданном диапазоне;
- логирования выполнения функций с помощью декоратора `log`;
- чтения финансовых транзакций из JSON-файла;
- получения суммы транзакции в рублях с конвертацией USD и EUR через внешний API.

## Структура проекта

```text
data/
    operations.json
src/
    masks.py
    widget.py
    processing.py
    generators.py
    decorators.py
    utils.py
    external_api.py
tests/
    test_masks.py
    test_widget.py
    test_processing.py
    test_generators.py
    test_decorators.py
    test_utils.py
    test_external_api.py
.env.example
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

4. Создайте файл `.env` на основе `.env.example` и укажите свой API-ключ:

```text
API_KEY=your_api_key_here
```

Файл `.env` содержит конфиденциальные данные и не добавляется в Git.

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
    {
        "state": "EXECUTED",
        "date": "2024-03-11T02:26:18.671407",
    },
    {
        "state": "CANCELED",
        "date": "2024-02-10T12:00:00.000000",
    },
]

result = filter_by_state(operations)
```

### Сортировка операций

```python
from src.processing import sort_by_date

operations = [
    {
        "state": "EXECUTED",
        "date": "2024-03-11T02:26:18.671407",
    },
    {
        "state": "CANCELED",
        "date": "2024-02-10T12:00:00.000000",
    },
]

result = sort_by_date(operations)
```

### Фильтрация транзакций по валюте

```python
from src.generators import filter_by_currency

transactions = [
    {
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        },
        "description": "Перевод организации",
    },
    {
        "operationAmount": {
            "currency": {
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

print(next(usd_transactions))
```

### Получение описаний транзакций

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)

print(next(descriptions))
print(next(descriptions))
```

### Генерация номеров банковских карт

```python
from src.generators import card_number_generator

card_numbers = card_number_generator(1, 3)

print(next(card_numbers))
print(next(card_numbers))
print(next(card_numbers))
```

### Логирование работы функций

Декоратор `log` позволяет записывать информацию о выполнении функции в консоль или файл.

```python
from src.decorators import log


@log()
def add_numbers(x, y):
    return x + y


add_numbers(1, 2)
```

Результат:

```text
add_numbers ok
```

Для записи лога в файл:

```python
@log(filename="mylog.txt")
def add_numbers(x, y):
    return x + y
```

При возникновении ошибки декоратор записывает имя функции, информацию об ошибке и переданные аргументы.

### Чтение транзакций из JSON-файла

Функция `load_transactions` загружает финансовые операции из JSON-файла.

```python
from src.utils import load_transactions

transactions = load_transactions("data/operations.json")

print(len(transactions))
```

Если файл отсутствует, пустой, содержит некорректный JSON или его содержимое не является списком, функция возвращает пустой список.

### Получение суммы транзакции в рублях

Функция `get_transaction_amount` принимает словарь с данными о транзакции и возвращает сумму операции в рублях.

Для операций в рублях сумма возвращается без конвертации. Для операций в USD и EUR выполняется запрос к Exchange Rates Data API.

```python
from src.external_api import get_transaction_amount

transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {
            "code": "RUB"
        },
    }
}

amount = get_transaction_amount(transaction)

print(amount)
```

Для работы конвертации необходимо указать API-ключ в файле `.env`.

## Тестирование

Для тестирования проекта используется библиотека `pytest`.

Тесты расположены в директории `tests`:

```text
tests/
    test_masks.py
    test_widget.py
    test_processing.py
    test_generators.py
    test_decorators.py
    test_utils.py
    test_external_api.py
```

Тесты функций работы с JSON-файлами и внешним API используют `Mock` и `patch`, чтобы не зависеть от реальных файлов и сетевых запросов.

Для запуска всех тестов:

```bash
pytest
```

Для проверки покрытия функционального кода тестами:

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

HTML-отчет создается в директории:

```text
htmlcov/
```

Для проверки оформления кода:

```bash
flake8
```

Для проверки сортировки импортов:

```bash
isort . --check-only
```

Для проверки типов:

```bash
mypy src
```

## Автор

Оксана Тишина
