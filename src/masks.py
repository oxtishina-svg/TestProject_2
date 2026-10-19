import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/masks.log",
    mode="w",
    encoding="utf-8",
)

file_formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s"
)

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты."""

    if len(card_number) != 16:
        logger.error(
            "Некорректная длина номера карты: %s символов",
            len(card_number),
        )
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_card_number = (
        f"{card_number[:4]} "
        f"{card_number[4:6]}** "
        f"**** "
        f"{card_number[-4:]}"
    )

    logger.info("Номер карты успешно замаскирован")

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета."""

    if len(account_number) != 20:
        logger.error(
            "Некорректная длина номера счета: %s символов",
            len(account_number),
        )
        raise ValueError("Номер счета должен содержать 20 цифр")

    masked_account_number = f"**{account_number[-4:]}"

    logger.info("Номер счета успешно замаскирован")

    return masked_account_number
