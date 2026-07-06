def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Возвращает список словарей с указанным значением ключа state."""

    result = []

    for item in data:
        if item["state"] == state:
            result.append(item)

    return result


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Сортирует список словарей по ключу date."""

    return sorted(data, key=lambda item: item["date"], reverse=reverse)

