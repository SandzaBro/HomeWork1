from masks import get_mask_account, get_mask_card_number


def mask_account_card(info_account_card: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""

    # Разделяем строку на части
    parts = info_account_card.split()

    # Проверка входных данных по кол-ву слов
    if len(parts) > 1:
        card_type = " ".join(parts[:-1])
        card_number = parts[-1]
    else:
        return info_account_card

    # Проверка наличия слова "Счет" в входных данных и их маскировка
    if "Счет" in card_type or "счет" in card_type:
        masked_number = get_mask_account(card_number)
        return f"{card_type} {masked_number}"
    else:
        masked_number = get_mask_card_number(card_number)
        return f"{card_type} {masked_number}"

# Проверяем
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""

    # Разбиваем строку по символу 'T' и берем первую часть (дату)
    date_part = date_string.split('T')[0]

    # Разбиваем дату по '-' и переставляем части
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"
