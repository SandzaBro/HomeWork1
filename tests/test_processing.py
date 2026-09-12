from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации со статусом по умолчанию 'EXECUTED'"""
    result = filter_by_state(sample_transactions)
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:00:00.000000"},
    ]
    assert result == expected


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2, 4]),
        ("PENDING", []),
        ("", []),
    ],
)
def test_filter_by_state_parametrized(
    sample_transactions: List[Dict[str, Any]], state: str, expected_ids: List[int]
) -> None:
    """Параметризованный тест для разных значений state"""
    result = filter_by_state(sample_transactions, state)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_filter_by_state_no_matching(only_executed_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование, когда нет словарей с указанным статусом"""
    result = filter_by_state(only_executed_transactions, "CANCELED")
    assert result == []


def test_filter_by_state_empty_list() -> None:
    """Тестирование на пустом списке"""
    assert filter_by_state([]) == []
    assert filter_by_state([], "CANCELED") == []


def test_filter_by_state_missing_state_key() -> None:
    """Тестирование, когда у некоторых словарей отсутствует ключ state"""
    transactions = [
        {"id": 1, "date": "2021-01-01"},
        {"id": 2, "state": "EXECUTED", "date": "2021-02-01"},
    ]
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_original_not_mutated(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование, что исходный список не изменяется"""
    original_copy = sample_transactions.copy()
    filter_by_state(sample_transactions)
    assert sample_transactions == original_copy


def test_sort_by_date_descending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по убыванию (по умолчанию)"""
    result = sort_by_date(sample_transactions)
    expected_ids = [4, 3, 2, 1]  # от самой новой к самой старой
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_sort_by_date_ascending(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по возрастанию."""
    result = sort_by_date(sample_transactions, sort_order=False)
    expected_ids = [1, 2, 3, 4]  # от самой старой к самой новой
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_sort_by_date_same_dates(transactions_with_same_dates: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки при одинаковых датах (порядок сохраняется)"""
    result = sort_by_date(transactions_with_same_dates)
    expected_ids = [1, 2, 3]
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_sort_by_date_invalid_formats(transactions_with_invalid_dates: List[Dict[str, Any]]) -> None:
    """Тестирование на некорректные форматы дат (сортировка по строке)"""
    result = sort_by_date(transactions_with_invalid_dates)
    assert len(result) == 3
    result_ids = [item["id"] for item in result]
    assert set(result_ids) == {1, 2, 3}


def test_sort_by_date_empty_list() -> None:
    """Тестирование на пустом списке"""
    assert sort_by_date([]) == []
    assert sort_by_date([], sort_order=False) == []


def test_sort_by_date_original_not_mutated(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование, что исходный список не изменяется"""
    original_copy = sample_transactions.copy()
    sort_by_date(sample_transactions)
    assert sample_transactions == original_copy


@pytest.mark.parametrize(
    "sort_order, expected_ids",
    [
        (True, [3, 2, 1]),
        (False, [1, 2, 3]),
    ],
)
def test_sort_by_date_parametrized(
    only_executed_transactions: List[Dict[str, Any]], sort_order: bool, expected_ids: List[int]
) -> None:
    """Параметризованный тест для обоих порядков сортировки"""
    result = sort_by_date(only_executed_transactions, sort_order=sort_order)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids
