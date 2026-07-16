def filter_by_state(list_dicts, state='EXECUTED'):

    """Функция принимает список словарей и опционально значение для ключа state(по умолчанию
       'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых
        ключ state соответствует указанному значению"""

    result = []
    for item in list_dicts:
        if item.get('state') == state:
            result.append(item)
    return result


# Входные данные
list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вывод функции со статусом по умолчанию 'EXECUTED'
executed_items = filter_by_state(list_dict)
print(executed_items)

# Вывод функции, если вторым аргументом передано 'CANCELED'
canceled_items = filter_by_state(list_dict, 'CANCELED')
print(canceled_items)
