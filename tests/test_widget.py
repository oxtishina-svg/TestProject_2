import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        (
            "Visa Platinum 7000792289606361",
            "Visa Platinum 7000 79** **** 6361",
        ),
        (
            "Maestro 1234567890123456",
            "Maestro 1234 56** **** 3456",
        ),
        (
            "Счет 73654108430135874305",
            "Счет **4305",
        ),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


@pytest.mark.parametrize(
    "account_card",
    [
        "Visa Platinum",
        "Счет 1234",
    ],
)
def test_mask_account_card_invalid_data(account_card: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(account_card)


def test_get_date_empty_string() -> None:
    with pytest.raises(ValueError):
        get_date("")
