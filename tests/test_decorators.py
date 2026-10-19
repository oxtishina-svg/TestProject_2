import pytest

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "add_numbers ok\n"


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error:" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    result = multiply(2, 3)

    assert result == 6
    assert log_file.read_text(encoding="utf-8") == "multiply ok\n"


def test_log_file_error(tmp_path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    log_content = log_file.read_text(encoding="utf-8")

    assert "divide error:" in log_content
    assert "Inputs: (1, 0), {}" in log_content
