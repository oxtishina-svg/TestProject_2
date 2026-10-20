import re
from collections import Counter
from typing import Any


def filter_by_state(
    operations: list,
    state: str = "EXECUTED",
) -> list:
    """Возвращает список операций с указанным статусом."""

    result = []

    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)

    return result


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Сортирует список словарей по ключу date."""

    return sorted(
        operations,
        key=lambda operation: operation["date"],
        reverse=reverse,
    )


def process_bank_search(
    transactions: list[dict[str, Any]],
    search: str,
) -> list[dict[str, Any]]:
    """Возвращает транзакции, содержащие строку поиска в описании."""

    result = []

    for transaction in transactions:
        description = str(transaction.get("description", ""))

        if re.search(search, description, flags=re.IGNORECASE):
            result.append(transaction)

    return result


def process_bank_operations(
    transactions: list[dict[str, Any]],
    categories: list[str],
) -> dict[str, int]:
    """Подсчитывает количество операций по заданным категориям."""

    descriptions = [
        str(transaction.get("description", ""))
        for transaction in transactions
    ]

    description_counter = Counter(descriptions)

    return {
        category: description_counter[category]
        for category in categories
    }
