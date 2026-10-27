from unittest.mock import Mock, patch

import pandas as pd

from src.data_processing import read_transactions_csv, read_transactions_excel


@patch("src.data_processing.pd.read_csv")
def test_read_transactions_csv(mock_read_csv: Mock) -> None:
    dataframe = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "amount": 1000.0,
            },
            {
                "id": 2,
                "state": "CANCELED",
                "amount": 500.0,
            },
        ]
    )

    mock_read_csv.return_value = dataframe

    result = read_transactions_csv("transactions.csv")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "amount": 1000.0,
        },
        {
            "id": 2,
            "state": "CANCELED",
            "amount": 500.0,
        },
    ]

    mock_read_csv.assert_called_once_with(
        "transactions.csv",
        sep=";",
    )


@patch("src.data_processing.pd.read_excel")
def test_read_transactions_excel(mock_read_excel: Mock) -> None:
    dataframe = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "amount": 1000.0,
            },
            {
                "id": 2,
                "state": "CANCELED",
                "amount": 500.0,
            },
        ]
    )

    mock_read_excel.return_value = dataframe

    result = read_transactions_excel("transactions.xlsx")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "amount": 1000.0,
        },
        {
            "id": 2,
            "state": "CANCELED",
            "amount": 500.0,
        },
    ]

    mock_read_excel.assert_called_once_with(
        "transactions.xlsx",
    )
