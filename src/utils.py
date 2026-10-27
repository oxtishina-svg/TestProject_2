import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/utils.log",
    mode="w",
    encoding="utf-8",
)

file_formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s"
)

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """Загружает список финансовых транзакций из JSON-файла."""

    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(
                "Успешно загружены транзакции из файла %s",
                file_path,
            )
            return data

        logger.error(
            "Данные в файле %s не являются списком",
            file_path,
        )
        return []

    except FileNotFoundError:
        logger.error(
            "Файл %s не найден",
            file_path,
        )
        return []

    except json.JSONDecodeError:
        logger.error(
            "Ошибка декодирования JSON в файле %s",
            file_path,
        )
        return []
