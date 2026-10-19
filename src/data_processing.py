from typing import Any, cast

import pandas as pd


def read_transactions_csv(file_path: str) -> list[dict[str, Any]]:
    """Считывает финансовые транзакции из CSV-файла."""

    dataframe = pd.read_csv(file_path, sep=";")
    dataframe = dataframe.dropna(how="all")

    records = dataframe.to_dict(orient="records")

    return cast(list[dict[str, Any]], records)


def read_transactions_excel(file_path: str) -> list[dict[str, Any]]:
    """Считывает финансовые транзакции из XLSX-файла."""

    dataframe = pd.read_excel(file_path)
    dataframe = dataframe.dropna(how="all")

    records = dataframe.to_dict(orient="records")

    return cast(list[dict[str, Any]], records)
