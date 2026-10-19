import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")

    if api_key is None:
        raise ValueError("API_KEY не найден в переменных окружения")

    headers = {
        "apikey": api_key,
    }

    params = {
        "amount": amount,
        "from": currency,
        "to": "RUB",
    }

    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers=headers,
        params=params,
    )

    result = response.json()

    return float(result["result"])
