import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> list[dict[str, str]]:
    return [
        {
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "state": "CANCELED",
            "date": "2019-04-04T23:20:05.206878",
        },
        {
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
        },
    ]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(
    operations: list[dict[str, str]],
    state: str,
    expected_count: int,
) -> None:
    result = filter_by_state(operations, state)

    assert len(result) == expected_count
    assert all(operation["state"] == state for operation in result)


def test_sort_by_date_descending(
    operations: list[dict[str, str]],
) -> None:
    result = sort_by_date(operations)

    assert result[0]["date"] == "2019-04-04T23:20:05.206878"
    assert result[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_ascending(
    operations: list[dict[str, str]],
) -> None:
    result = sort_by_date(operations, reverse=False)

    assert result[0]["date"] == "2018-06-30T02:08:58.425572"
    assert result[-1]["date"] == "2019-04-04T23:20:05.206878"


def test_sort_by_date_equal_dates() -> None:
    operations = [
        {"date": "2024-01-01T12:00:00", "state": "EXECUTED"},
        {"date": "2024-01-01T12:00:00", "state": "CANCELED"},
    ]

    result = sort_by_date(operations)

    assert result == operations


def test_filter_by_state_empty_list() -> None:
    assert filter_by_state([]) == []


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []
