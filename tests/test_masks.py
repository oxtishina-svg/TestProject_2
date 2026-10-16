import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "",
        "1234",
        "123456789012345",
        "12345678901234567",
    ],
)
def test_get_mask_card_number_invalid_length(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number",
    [
        "",
        "1234",
        "1234567890123456789",
        "123456789012345678901",
    ],
)
def test_get_mask_account_invalid_length(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
