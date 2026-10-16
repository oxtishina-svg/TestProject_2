from typing import Any

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


Transaction = dict[str, Any]


@pytest.fixture
def transactions() -> list[Transaction]:
    return [
        {
            "operationAmount": {
                "currency": {
                    "code": "USD",
                }
            },
            "description": "Перевод организации",
        },
        {
            "operationAmount": {
                "currency": {
                    "code": "RUB",
                }
            },
            "description": "Перевод со счета на счет",
        },
        {
            "operationAmount": {
                "currency": {
                    "code": "USD",
                }
            },
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency(
    transactions: list[Transaction],
) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")

    assert next(usd_transactions)["description"] == "Перевод организации"
    assert next(usd_transactions)["description"] == "Перевод с карты на карту"


def test_filter_by_currency_no_matches(
    transactions: list[Transaction],
) -> None:
    eur_transactions = filter_by_currency(transactions, "EUR")

    with pytest.raises(StopIteration):
        next(eur_transactions)


def test_transaction_descriptions(
    transactions: list[Transaction],
) -> None:
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_transaction_descriptions_empty() -> None:
    descriptions = transaction_descriptions([])

    with pytest.raises(StopIteration):
        next(descriptions)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(
    start: int,
    stop: int,
    expected: list[str],
) -> None:
    assert list(card_number_generator(start, stop)) == expected
