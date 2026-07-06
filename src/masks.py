def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты."""
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета."""
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

#test_commit