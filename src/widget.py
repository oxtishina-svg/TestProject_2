from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Маскирует номер карты или счета."""

    name = " ".join(account_card.split()[:-1])
    number = account_card.split()[-1]

    if name == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"