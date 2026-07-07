def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""

    # Преобразуем в строку, если пришло число
    card_str = str(card_number)

    # Проверяем длину номера карты
    if len(card_str) < 16:
        return card_str

    # Отображение первых 6 цифр и последних 4 цифр
    first_six = card_str[:6]
    last_four = card_str[-4:]

    # Формируем маску в формате XXXX XX** **** XXXX
    masked = f"{first_six[:4]} {first_six[4:]}** **** {last_four}"

    return masked


# Проверяем
print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера."""

    # Преобразуем в строку, если пришло число
    account_str = str(account_number)

    # Проверяем длину номера карты
    if len(account_str) < 4:
        return account_str

    # Отображение последних 4 цифр
    last_four = account_str[-4:]

    # Формируем маску в формате **XXXX
    return f"**{last_four}"


# Проверяем
print(get_mask_account("73654108430135874305"))
print(get_mask_account("73654108430135875768"))
