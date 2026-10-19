from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount_rub() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "RUB",
            },
        }
    }

    result = get_transaction_amount(transaction)

    assert result == 100.0


@patch("src.external_api.requests.get")
def test_get_transaction_amount_usd(mock_get: Mock) -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD",
            },
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {
        "result": 9200.0,
    }
    mock_get.return_value = mock_response

    result = get_transaction_amount(transaction)

    assert result == 9200.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_get_transaction_amount_eur(mock_get: Mock) -> None:
    transaction = {
        "operationAmount": {
            "amount": "50.00",
            "currency": {
                "code": "EUR",
            },
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {
        "result": 5000.0,
    }
    mock_get.return_value = mock_response

    result = get_transaction_amount(transaction)

    assert result == 5000.0
    mock_get.assert_called_once()
