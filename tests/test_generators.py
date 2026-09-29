from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
    ],
    ids=["usd", "rub"],
)
def test_filters_by_currency(transactions: List[Dict[str, Any]], currency: str, expected_ids: List[int]) -> None:
    """Параметризованный тест функции, которая корректно фильтрует транзакции по заданной валюте"""
    result = list(filter_by_currency(transactions, currency))
    assert [t["id"] for t in result] == expected_ids
    assert all(t["operationAmount"]["currency"]["code"] == currency for t in result)


@pytest.mark.parametrize(
    "currency",
    ["EUR", "JPY", "usd", ""],
    ids=["eur", "jpy", "lowercase-usd", "empty"],
)
def test_filters_by_currency_missing(transactions: List[Dict[str, Any]], currency: str) -> None:
    """Параметризованный тест, обрабатывающий случаи, когда транзакции в заданной валюте отсутствуют"""
    assert list(filter_by_currency(transactions, currency)) == []


@pytest.mark.parametrize(
    "start, stop, expected_len",
    [
        (1, 1, 1),
        (1, 5, 5),
        (1, 100, 100),
        (10, 12, 3),
    ],
    ids=["single", "five", "hundred", "three"],
)
def test_card_number_generator_range_length(start: int, stop: int, expected_len: int) -> None:
    """Параметризованный тест, проверяющий, что длина выдачи совпадает с размером диапазона"""
    assert len(list(card_number_generator(start, stop))) == expected_len


@pytest.mark.parametrize(
    "start, stop",
    [
        (1, 10),
        (9999_9999_9999_9998, 9999_9999_9999_9999),
    ],
    ids=["small-range", "top-range"],
)
def test_card_number_generator_format(start: int, stop: int) -> None:
    """Параметризованный тест, проверяющий каждый номер — 4 группы по 4 цифры"""
    for card in card_number_generator(start, stop):
        parts = card.split(" ")
        assert len(parts) == 4
        assert all(len(p) == 4 and p.isdigit() for p in parts)
        assert len(card) == 19


# def test_returns_iterator(self, transactions: List[Dict[str, Any]]) -> None:
#     """Тестирование функции, которая возвращает итератор (генератор), поддерживающий next()."""
#     result = filter_by_currency(transactions, "USD")
#     assert isinstance(result, Generator)
#     assert next(result)["id"] == 939719570


def test_filters_by_currency_default_usd(transactions: List[Dict[str, Any]]) -> None:
    """Тестирование, когда не указана валюта (по умолчанию используется USD)"""
    assert list(filter_by_currency(transactions)) == list(filter_by_currency(transactions, "USD"))


def test_filters_by_currency_empty_list(empty_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование пустого списка"""
    assert list(filter_by_currency(empty_transactions, "USD")) == []


def test_filters_by_currency_without_currency(transactions_without_currency_field: List[Dict[str, Any]]) -> None:
    """Тестирование транзакции без currency пропускаются без исключений."""
    assert list(filter_by_currency(transactions_without_currency_field, "USD")) == []


def test_transaction_descriptions_all(transactions: List[Dict[str, Any]], expected_descriptions: List[str]) -> None:
    """Тестирование базового набора описания выдаются по порядку и совпадают с ожидаемыми."""
    assert list(transaction_descriptions(transactions)) == expected_descriptions


def test_transaction_descriptions_empty_list(empty_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование пустого списка"""
    assert list(transaction_descriptions(empty_transactions)) == []


# def test_transaction_descriptions_without_description() -> None:
#     """Тестирование, если ключ description отсутствует"""
#     broken: List[Dict[str, Any]] = [{"id": 1}, {"id": 2, "description": ""}]
#     assert list(transaction_descriptions(broken)) == ["", ""]


# def test_stops_iteration(self, transactions: List[Dict[str, Any]]) -> None:
#     """После выдачи всех описаний генератор бросает StopIteration."""
#     gen = transaction_descriptions(transactions)
#     for _ in range(len(transactions)):
#         next(gen)
#     with pytest.raises(StopIteration):
#         next(gen)


def test_card_number_generator_1_to_5() -> None:
    """Тестирование диапазона от 1 до 5"""
    assert list(card_number_generator(1, 5)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_min_edge() -> None:
    """Тестирование корректной нижней границы диапазона (0000 0000 0000 0001)"""
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]


def test_card_number_generator_max_edge() -> None:
    """Тестирование корректной верхней границы диапазона (9999 9999 9999 9999)"""
    result = list(card_number_generator(9999_9999_9999_9999, 9999_9999_9999_9999))
    assert result == ["9999 9999 9999 9999"]


def test_card_number_generator_empty_range() -> None:
    """Тестирование случая, когда start > stop"""
    assert list(card_number_generator(5, 1)) == []
