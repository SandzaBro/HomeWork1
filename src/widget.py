from src.masks import get_mask_account, get_mask_card_number


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
    if "счет" in card_type.lower():
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

    # Находим разделитель даты и времени (T или пробел)
    if "T" in date_string:
        date_part = date_string.split("T")[0]
    elif " " in date_string:
        date_part = date_string.split(" ")[0]
    else:
        date_part = date_string

    # Определяем разделитель даты (-, / или .)
    parts = []  # Инициализируем переменную parts
    if "-" in date_part:
        parts = date_part.split("-")
    elif "/" in date_part:
        parts = date_part.split("/")
    elif "." in date_part:
        parts = date_part.split(".")
    else:
        # Если разделитель не найден, возвращаем исходную строку
        return date_string

    # Проверяем, что есть все три части (год, месяц, день)
    if len(parts) >= 3:
        year, month, day = parts[0], parts[1], parts[2]
        return f"{day}.{month}.{year}"
    else:
        # Если не хватает частей, возвращаем исходную строку
        return date_string


# Проверяем
print(get_date("2024-03-11T02:26:18.671407"))
