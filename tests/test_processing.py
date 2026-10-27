from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state():
    operations = [
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
        {"state": "EXECUTED"},
    ]

    result = filter_by_state(operations)

    assert result == [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
    ]


def test_filter_by_state_canceled():
    operations = [
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
    ]

    result = filter_by_state(operations, "CANCELED")

    assert result == [{"state": "CANCELED"}]


def test_sort_by_date():
    operations = [
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2019-04-04T23:20:05.206878"},
        {"date": "2019-03-23T01:09:46.296404"},
    ]

    result = sort_by_date(operations)

    assert result == [
        {"date": "2019-04-04T23:20:05.206878"},
        {"date": "2019-03-23T01:09:46.296404"},
        {"date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending():
    operations = [
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2019-04-04T23:20:05.206878"},
    ]

    result = sort_by_date(operations, reverse=False)

    assert result == [
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2019-04-04T23:20:05.206878"},
    ]


def test_process_bank_search() -> None:
    transactions = [
        {
            "description": "Перевод организации",
        },
        {
            "description": "Открытие вклада",
        },
        {
            "description": "Перевод со счета на счет",
        },
    ]

    result = process_bank_search(
        transactions,
        "перевод",
    )

    assert result == [
        {
            "description": "Перевод организации",
        },
        {
            "description": "Перевод со счета на счет",
        },
    ]


def test_process_bank_search_no_matches() -> None:
    transactions = [
        {
            "description": "Открытие вклада",
        },
    ]

    result = process_bank_search(
        transactions,
        "перевод",
    )

    assert result == []


def test_process_bank_operations() -> None:
    transactions = [
        {
            "description": "Перевод организации",
        },
        {
            "description": "Перевод организации",
        },
        {
            "description": "Открытие вклада",
        },
    ]

    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод со счета на счет",
    ]

    result = process_bank_operations(
        transactions,
        categories,
    )

    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод со счета на счет": 0,
    }
