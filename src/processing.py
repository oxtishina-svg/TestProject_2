def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Возвращает список словарей с указанным значением ключа state."""

    result = []

    for operation in operations:
        if operation["state"] == state:
            result.append(operation)

    return result


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Сортирует список словарей по ключу date."""

    return sorted(
        operations,
        key=lambda operation: operation["date"],
        reverse=reverse,
    )
