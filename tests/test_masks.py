import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(valid_card: str) -> None:
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(valid_card) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_different_cards(card_number: str, expected: str) -> None:
    """Тестирование маскировки разных номеров карт"""
    assert get_mask_card_number(card_number) == expected


# Проверка работы функции на различных входных форматах номеров карт
@pytest.mark.parametrize("card_number", ["123456789012345", "12345678901234", "123"])
def test_get_mask_card_number_short(card_number: str) -> None:
    """Тестирование коротких номеров карт"""
    assert get_mask_card_number(card_number) == card_number


@pytest.mark.parametrize("card_number", ["", " ", "abcd"])
def test_get_mask_card_number_invalid_strings(card_number: str) -> None:
    """Тестирование некорректных строк"""
    assert get_mask_card_number(card_number) == card_number


def test_get_mask_account(account_number: str) -> None:
    """Тестирование маскировки номера счета"""
    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize(
    "account_number, expected", [("73654108430135874305", "**4305"), ("12345678", "**5678"), ("9999", "**9999")]
)
def test_get_mask_account_parametrize(account_number: str, expected: str) -> None:
    """Параметризованный тест маскировки счетов"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", ["", "1", "12", "123"])
def test_get_mask_account_invalid_data(account_number: str) -> None:
    """Тестирование некорректных номеров счетов"""
    assert get_mask_account(account_number) == account_number
