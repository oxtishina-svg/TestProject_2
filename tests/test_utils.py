import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_transactions_success() -> None:
    test_data = [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "RUB"},
            },
        }
    ]

    mock_file = mock_open(read_data=json.dumps(test_data))

    with patch("builtins.open", mock_file):
        result = load_transactions("operations.json")

    assert result == test_data


def test_load_transactions_empty_file() -> None:
    mock_file = mock_open(read_data="")

    with patch("builtins.open", mock_file):
        result = load_transactions("operations.json")

    assert result == []


def test_load_transactions_not_list() -> None:
    test_data = {"id": 1}

    mock_file = mock_open(read_data=json.dumps(test_data))

    with patch("builtins.open", mock_file):
        result = load_transactions("operations.json")

    assert result == []


def test_load_transactions_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("missing.json")

    assert result == []
