from unittest.mock import Mock, patch

from src.main import main, print_transaction


@patch("src.main.load_transactions")
def test_main_json(mock_load_transactions: Mock) -> None:
    mock_load_transactions.return_value = [
        {
            "state": "EXECUTED",
            "date": "2019-01-01T00:00:00.000000",
            "description": "Открытие вклада",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "code": "RUB",
                },
            },
            "to": "Счет 12345678901234567890",
        },
    ]

    user_answers = [
        "1",
        "EXECUTED",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "builtins.input",
        side_effect=user_answers,
    ):
        main()

    mock_load_transactions.assert_called_once_with(
        "data/operations.json"
    )


@patch("src.main.load_transactions")
def test_main_repeats_invalid_state(
    mock_load_transactions: Mock,
) -> None:
    mock_load_transactions.return_value = [
        {
            "state": "EXECUTED",
            "date": "2019-01-01T00:00:00.000000",
            "description": "Открытие вклада",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "code": "RUB",
                },
            },
            "to": "Счет 12345678901234567890",
        },
    ]

    user_answers = [
        "1",
        "test",
        "EXECUTED",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "builtins.input",
        side_effect=user_answers,
    ):
        main()


@patch("src.main.load_transactions")
def test_main_empty_result(
    mock_load_transactions: Mock,
    capsys,
) -> None:
    mock_load_transactions.return_value = [
        {
            "state": "CANCELED",
            "date": "2019-01-01T00:00:00.000000",
            "description": "Открытие вклада",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "code": "RUB",
                },
            },
            "to": "Счет 12345678901234567890",
        },
    ]

    user_answers = [
        "1",
        "EXECUTED",
        "нет",
        "нет",
        "нет",
    ]

    with patch(
        "builtins.input",
        side_effect=user_answers,
    ):
        main()

    captured = capsys.readouterr()

    assert "Не найдено ни одной транзакции" in captured.out


def test_print_transaction_without_sender(capsys) -> None:
    transaction = {
        "state": "EXECUTED",
        "date": "2019-01-01T00:00:00.000000",
        "description": "Открытие вклада",
        "amount": 1000.0,
        "currency_code": "RUB",
        "from": float("nan"),
        "to": "Счет 12345678901234567890",
    }

    print_transaction(transaction)

    captured = capsys.readouterr()

    assert "Счет **7890" in captured.out
    assert "Сумма: 1000.0 RUB" in captured.out
