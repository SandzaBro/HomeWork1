from typing import Any, Dict, List


def filter_by_state(list_of_transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:

    """Функция принимает список словарей и опционально значение для ключа state(по умолчанию
       'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых
        ключ state соответствует указанному значению"""

    result = []
    for item in list_of_transactions:
        if item.get('state') == state:
            result.append(item)
    return result


# Входные данные
list_of_transaction = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вывод функции со статусом по умолчанию 'EXECUTED'
executed_items = filter_by_state(list_of_transaction)
print(executed_items)

# Вывод функции, если вторым аргументом передано 'CANCELED'
canceled_items = filter_by_state(list_of_transaction, 'CANCELED')
print(canceled_items)


def sort_by_date(transactions: List[Dict[str, Any]], argument: bool = True) -> List[Dict[str, Any]]:

    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и возвращает новый список,
    отсортированный по дате (date)."""

    return sorted(transactions, key=lambda x: x['date'], reverse=argument)


# Список транзакций
list_of_transaction = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Сортировка по убыванию (по умолчанию)
sorting_result = sort_by_date(list_of_transaction)
print(sorting_result)
