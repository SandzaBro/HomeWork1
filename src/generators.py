from typing import Any, Dict, Iterator, List

from src.check_example_generators import transactions


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)"""

    for transaction in transactions:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency:
            yield transaction


# Пример использования функции
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Функция, который принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction.get("description", "")


# Пример использования функции
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция-генератор, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""

    for number in range(start, stop + 1):
        digits = f"{number:016d}"
        yield f"{digits[:4]} {digits[4:8]} {digits[8:12]} {digits[12:]}"


# Пример использования функции
for card_number in card_number_generator(1, 5):
    print(card_number)
