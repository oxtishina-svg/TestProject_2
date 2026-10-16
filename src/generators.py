def filter_by_currency(transactions: list, currency: str):
    """Возвращает транзакции с указанной валютой по одной."""

    for transaction in transactions:
        transaction_currency = transaction["operationAmount"]["currency"]["code"]

        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list):
    """Возвращает описания транзакций по одному."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int):
    """Генерирует номера банковских карт в заданном диапазоне."""

    for card_number in range(start, stop + 1):
        number = str(card_number).zfill(16)

        yield (
            f"{number[:4]} "
            f"{number[4:8]} "
            f"{number[8:12]} "
            f"{number[12:]}"
        )
