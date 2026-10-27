from typing import Any

import pandas as pd

from src.data_processing import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def get_currency_code(transaction: dict[str, Any]) -> str:
    """Возвращает код валюты транзакции."""

    if "operationAmount" in transaction:
        return str(
            transaction["operationAmount"]["currency"]["code"]
        )

    return str(transaction.get("currency_code", ""))


def get_transaction_amount(transaction: dict[str, Any]) -> str:
    """Возвращает сумму транзакции."""

    if "operationAmount" in transaction:
        return str(transaction["operationAmount"]["amount"])

    return str(transaction.get("amount", ""))


def print_transaction(transaction: dict[str, Any]) -> None:
    """Выводит информацию об одной транзакции."""

    date = get_date(str(transaction["date"]))
    description = str(transaction.get("description", ""))

    print(f"{date} {description}")

    sender = transaction.get("from")
    receiver = transaction.get("to")

    has_sender = sender is not None and pd.notna(sender)
    has_receiver = receiver is not None and pd.notna(receiver)

    if has_sender and has_receiver:
        print(
            f"{mask_account_card(str(sender))} -> "
            f"{mask_account_card(str(receiver))}"
        )
    elif has_receiver:
        print(mask_account_card(str(receiver)))

    amount = get_transaction_amount(transaction)
    currency = get_currency_code(transaction)

    print(f"Сумма: {amount} {currency}")
    print()


def main() -> None:
    """Запускает консольный интерфейс работы с транзакциями."""

    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Пользователь: ").strip()

    if file_choice == "1":
        transactions = load_transactions(
            "data/operations.json"
        )
        print("Для обработки выбран JSON-файл.")

    elif file_choice == "2":
        transactions = read_transactions_csv(
            "data/transactions.csv"
        )
        print("Для обработки выбран CSV-файл.")

    elif file_choice == "3":
        transactions = read_transactions_excel(
            "data/transactions_excel.xlsx"
        )
        print("Для обработки выбран XLSX-файл.")

    else:
        print("Некорректный пункт меню.")
        return

    available_states = {
        "EXECUTED",
        "CANCELED",
        "PENDING",
    }

    while True:
        print(
            "Введите статус, по которому необходимо "
            "выполнить фильтрацию."
        )
        print(
            "Доступные для фильтровки статусы: "
            "EXECUTED, CANCELED, PENDING"
        )

        state = input("Пользователь: ").strip().upper()

        if state in available_states:
            break

        print(
            f'Статус операции "{state}" недоступен.'
        )

    transactions = filter_by_state(
        transactions,
        state,
    )

    print(
        f'Операции отфильтрованы по статусу "{state}"'
    )

    sort_answer = input(
        "Отсортировать операции по дате? Да/Нет\n"
    ).strip().lower()

    if sort_answer == "да":
        sort_order = input(
            "Отсортировать по возрастанию "
            "или по убыванию?\n"
        ).strip().lower()

        reverse = sort_order == "по убыванию"

        transactions = sort_by_date(
            transactions,
            reverse=reverse,
        )

    rub_answer = input(
        "Выводить только рублевые транзакции? Да/Нет\n"
    ).strip().lower()

    if rub_answer == "да":
        transactions = [
            transaction
            for transaction in transactions
            if get_currency_code(transaction) == "RUB"
        ]

    search_answer = input(
        "Отфильтровать список транзакций "
        "по определенному слову в описании? Да/Нет\n"
    ).strip().lower()

    if search_answer == "да":
        search = input(
            "Введите строку для поиска:\n"
        ).strip()

        transactions = process_bank_search(
            transactions,
            search,
        )

    print(
        "Распечатываю итоговый список транзакций..."
    )
    print()

    if not transactions:
        print(
            "Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
        return

    print(
        "Всего банковских операций в выборке: "
        f"{len(transactions)}"
    )
    print()

    for transaction in transactions:
        print_transaction(transaction)


if __name__ == "__main__":
    main()
