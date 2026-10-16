import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "card_number",
    [
        "1234",
        "123456789012345",
        "12345678901234567",
    ],
)
def test_get_mask_card_number_invalid_length(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number",
    [
        "1234",
        "1234567890123456789",
        "123456789012345678901",
    ],
)
def test_get_mask_account_invalid_length(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)
