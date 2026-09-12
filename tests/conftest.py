from typing import Any, Dict, List

import pytest


@pytest.fixture
def valid_card() -> str:
    """Фикстура с корректным номером карты"""
    return "7000792289606361"


@pytest.fixture
def account_number() -> str:
    """Фикстура с корректным номером счета"""
    return "73654108430135874305"


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с разными комбинациями статусов и дат."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-02-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:00:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2021-04-01T16:00:00.000000"},
    ]


@pytest.fixture
def only_executed_transactions() -> List[Dict[str, Any]]:
    """Фикстура со всеми EXECUTED."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2021-02-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:00:00.000000"},
    ]


@pytest.fixture
def only_canceled_transactions() -> List[Dict[str, Any]]:
    """Фикстура со всеми CANCELED."""
    return [
        {"id": 1, "state": "CANCELED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-02-01T12:00:00.000000"},
    ]


@pytest.fixture
def transactions_with_same_dates() -> List[Dict[str, Any]]:
    """Фикстура с одинаковыми датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
    ]


@pytest.fixture
def transactions_with_invalid_dates() -> List[Dict[str, Any]]:
    """Фикстура с некорректными форматами дат."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "not-a-date"},
        {"id": 2, "state": "CANCELED", "date": "2021/02/01"},
        {"id": 3, "state": "EXECUTED", "date": ""},
    ]
