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
    """Фикстура с разными комбинациями статусов и дат"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-02-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:00:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2021-04-01T16:00:00.000000"},
    ]


@pytest.fixture
def only_executed_transactions() -> List[Dict[str, Any]]:
    """Фикстура со всеми EXECUTED"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2021-02-01T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-03-01T14:00:00.000000"},
    ]


@pytest.fixture
def only_canceled_transactions() -> List[Dict[str, Any]]:
    """Фикстура со всеми CANCELED"""
    return [
        {"id": 1, "state": "CANCELED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-02-01T12:00:00.000000"},
    ]


@pytest.fixture
def transactions_with_same_dates() -> List[Dict[str, Any]]:
    """Фикстура с одинаковыми датами"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2021-01-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-01T10:00:00.000000"},
    ]


@pytest.fixture
def transactions_with_invalid_dates() -> List[Dict[str, Any]]:
    """Фикстура с некорректными форматами дат"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "not-a-date"},
        {"id": 2, "state": "CANCELED", "date": "2021/02/01"},
        {"id": 3, "state": "EXECUTED", "date": ""},
    ]


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """Фикстура со списком транзакций"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def empty_transactions() -> List[Dict[str, Any]]:
    """Фикстура пустого списка"""
    return []


@pytest.fixture
def transactions_without_target_currency() -> List[Dict[str, Any]]:
    """Фикстура для списока транзакций без валюты USD"""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"name": "евро", "code": "EUR"}},
            "description": "Перевод со счета на счет",
        },
    ]


@pytest.fixture
def transactions_without_currency_field() -> List[Dict[str, Any]]:
    """Фикстура для транзакций без поля currency"""
    return [
        {"id": 1, "description": "нет operationAmount"},
        {"id": 2, "operationAmount": {}},
        {"id": 3, "operationAmount": {"currency": {}}},
    ]


@pytest.fixture
def expected_descriptions() -> List[str]:
    """Фикстура ожидаемой последовательности описаний для базового набора транзакций"""
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
