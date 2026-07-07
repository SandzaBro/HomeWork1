from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(info_account_card: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""

    # Разделяем строку на части
    parts = info_account_card.split()

    # Проверяем, что строка не пустая
    if not parts:
        return info_account_card

    # Определяем тип (последнее слово - это номер)
    # Если в строке больше 2 слов (например, "Visa Platinum"), объединяем все кроме последнего
    if len(parts) > 1:
        card_type = " ".join(parts[:-1])  # Все слова кроме последнего - это тип
        card_number = parts[-1]  # Последнее слово - это номер
    else:
        # Если только одно слово, считаем его номером
        return info_account_card

    # Проверяем, является ли строка счетом
    if "Счет" in card_type or "счет" in card_type:
        # Маскируем как счет
        masked_number = get_mask_account(card_number)
        return f"{card_type} {masked_number}"
    else:
        # Маскируем как карту
        masked_number = get_mask_card_number(card_number)
        return f"{card_type} {masked_number}"


print(mask_account_card("Visa Platinum 7000792289606361"))