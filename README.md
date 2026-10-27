# Учебный проект обработки банковских операций

## Описание

Проект содержит функции для обработки и анализа информации о банковских картах, счетах и финансовых операциях.

В проекте реализованы:
- маскировка номера банковской карты;
- маскировка номера банковского счета;
- определение типа платежного инструмента и его маскировка;
- преобразование даты к удобному формату;
- фильтрация операций по статусу;
- сортировка операций по дате;
- фильтрация транзакций по валюте с использованием генератора;
- последовательное получение описаний транзакций;
- генерация номеров банковских карт;
- логирование работы функций;
- загрузка финансовых операций из JSON-файла;
- загрузка финансовых операций из CSV-файла;
- загрузка финансовых операций из XLSX-файла;
- получение суммы транзакции в рублях с конвертацией валют через внешний API; 
- поиск банковских операций по строке в описании с использованием регулярных выражений;
- подсчет количества операций по заданным категориям;
- консольный интерфейс для работы с транзакциями из JSON, CSV и XLSX.

## Структура проекта

```text
data/
    operations.json
    transactions.csv
    transactions_excel.xlsx

logs/
    masks.log
    utils.log

src/
    main.py
    masks.py
    widget.py
    processing.py
    generators.py
    decorators.py
    utils.py
    external_api.py
    data_processing.py

tests/
    test_masks.py
    test_widget.py
    test_processing.py
    test_generators.py
    test_decorators.py
    test_utils.py
    test_external_api.py
    test_data_processing.py

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

В проекте используются библиотеки `requests`, `python-dotenv`, `pandas` и `openpyxl`.

Для работы с CSV- и Excel-файлами используется библиотека `pandas`. Для чтения XLSX-файлов дополнительно используется `openpyxl`.

## Переменные окружения

Создайте файл `.env` на основе `.env.example`:

```text
API_KEY=your_api_key_here
```

В `.env` необходимо указать API-ключ для сервиса конвертации валют.

Файл `.env` содержит конфиденциальные данные и не добавляется в Git.

## Использование

### Маскировка номера карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
```

### Маскировка номера счета

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

### Фильтрация операций по статусу

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

### Сортировка операций по дате

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

Декоратор `log` позволяет записывать информацию о выполнении функций в консоль или файл.

```python
from src.decorators import log


@log()
def add_numbers(x, y):
    return x + y


add_numbers(1, 2)
```

Также логирование используется в модулях `masks` и `utils`.

Логи записываются в директорию:

```text
logs/
```

Для модуля `masks` используется файл:

```text
logs/masks.log
```

Для модуля `utils`:

```text
logs/utils.log
```

Логи содержат дату и время, имя модуля, уровень сообщения и описание события.

### Чтение транзакций из JSON

Функция `load_transactions` загружает финансовые операции из JSON-файла.

```python
from src.utils import load_transactions

transactions = load_transactions("data/operations.json")

print(len(transactions))
```

Если файл отсутствует, содержит некорректный JSON или данные не являются списком, функция возвращает пустой список.

### Чтение транзакций из CSV

Функция `read_transactions_csv` считывает финансовые операции из CSV-файла и возвращает список словарей.

```python
from src.data_processing import read_transactions_csv

transactions = read_transactions_csv(
    "data/transactions.csv"
)

print(len(transactions))
```

Для чтения CSV-файла используется `pandas.read_csv()`.

### Чтение транзакций из Excel

Функция `read_transactions_excel` считывает финансовые операции из XLSX-файла и возвращает список словарей.

```python
from src.data_processing import read_transactions_excel

transactions = read_transactions_excel(
    "data/transactions_excel.xlsx"
)

print(len(transactions))
```

Для чтения Excel-файла используется `pandas.read_excel()`.

### Получение суммы транзакции в рублях

Функция `get_transaction_amount` принимает данные транзакции и возвращает сумму операции в рублях.

Для операций в RUB сумма возвращается без конвертации. Для операций в иностранной валюте используется внешний API конвертации валют.

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

Для работы функции необходимо указать API-ключ в файле `.env`.

## Тестирование

Для тестирования проекта используется `pytest`.

Тесты находятся в директории:

```text
tests/
```

Для новых функций чтения CSV- и XLSX-файлов используются `Mock` и `patch`.

Запуск всех тестов:

```bash
pytest
```

Проверка покрытия кода тестами:

```bash
pytest --cov=src --cov-report=term-missing
```

Требуемое покрытие функционального кода составляет не менее 80%.

## Проверка качества кода

Проверка кода с помощью Flake8:

```bash
flake8
```

Проверка сортировки импортов:

```bash
isort . --check-only
```

Проверка типов:

```bash
mypy src
```

### Поиск транзакций по описанию

Функция `process_bank_search` выполняет поиск банковских операций по строке в поле `description`.

```python
from src.processing import process_bank_search

transactions = [
    {"description": "Перевод организации"},
    {"description": "Открытие вклада"},
]

result = process_bank_search(
    transactions,
    "перевод",
)
```

Поиск выполняется с использованием регулярных выражений и не зависит от регистра.

### Подсчет операций по категориям

Функция `process_bank_operations` подсчитывает количество операций каждой указанной категории.

```python
from src.processing import process_bank_operations

categories = [
    "Перевод организации",
    "Открытие вклада",
]

result = process_bank_operations(
    transactions,
    categories,
)
```

Функция возвращает словарь, где ключами являются категории операций, а значениями их количество.

### Консольный интерфейс

Для запуска программы:

```bash
python -m src.main
```

Программа позволяет:
- выбрать источник данных JSON, CSV или XLSX;
- отфильтровать операции по статусу;
- отсортировать операции по дате;
- оставить только рублевые транзакции;
- выполнить поиск по описанию;
- вывести итоговый список операций.

## Автор

Оксана Тишина
