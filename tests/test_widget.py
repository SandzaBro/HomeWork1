import pytest

from src.widget import mask_account_card, get_date


# Параметризованные тесты для карт (проверяем логику распознавания типа)
@pytest.mark.parametrize("input_data, expected_output", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("American Express 1234567890123456", "American Express 1234 56** **** 3456"),
])
def test_mask_account_card_types_card(input_data, expected_output):
    """Тестирование маскировки различных типов карт"""
    assert mask_account_card(input_data) == expected_output


# Параметризованные тесты для счетов
@pytest.mark.parametrize("input_data, expected_output", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("счет 12345678901234567890", "счет **7890"),
    ("СчЕт 98765432109876543210", "СчЕт **3210"),
    ("СЧЕТ 12345678901234567890", "СЧЕТ **7890"),
])
def test_mask_account_card_types_account(input_data, expected_output):
    """Тестирование маскировки счетов"""
    assert mask_account_card(input_data) == expected_output


# Тест на обработку некорректных данных
@pytest.mark.parametrize("invalid_input", [
    "",  # Пустая строка
    "12345",  # Только номер
    "Карта",  # Только тип
    "   ",  # Пробелы
    "Visa",  # Только тип карты без номера
    "Счет",  # Только тип счета без номера
    "MasterCard 123",  # Короткий номер
    "Visa Classic abcdefghijklmnop",  # Нецифровой номер
])
def test_mask_account_card_invalid_input(invalid_input):
    """Тестирование устойчивости к некорректным входным данным"""
    # Функция должна вернуть исходную строку или не упасть
    result = mask_account_card(invalid_input)
    assert isinstance(result, str)


# Параметризованные тесты для различных дат
@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T15:30:45.123456", "25.12.2023"),
    ("2022-01-01T00:00:00.000000", "01.01.2022"),
    ("2024-02-29T12:00:00.000000", "29.02.2024"),  # Високосный год
    ("2021-07-15T23:59:59.999999", "15.07.2021"),
    ("2000-06-30T08:15:22.111222", "30.06.2000"),
])
def test_get_date_valid_dates(input_date, expected_output):
    """Тестирование корректного преобразования дат"""
    assert get_date(input_date) == expected_output


# Тесты с разными форматами разделителей
@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11", "11.03.2024"),  # Без времени
    ("2024/03/11T02:26:18.671407", "11.03.2024"),  # С другими разделителями
    ("2024.03.11T02:26:18.671407", "11.03.2024"),  # С точками
    ("2024-03-11T02:26:18", "11.03.2024"),  # Без микросекунд
    ("2024-3-11T02:26:18.671407", "11.3.2024"),  # Месяц без ведущего нуля
    ("2024-03-1T02:26:18.671407", "1.03.2024"),  # День без ведущего нуля
])
def test_get_date_different_formats(input_date, expected_output):
    """Тестирование работы с разными форматами даты"""
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize("input_date, expected_output", [
    ("2024/03/11T02:26:18.671407", "11.03.2024"),  # С другими разделителями
    ("2024.03.11T02:26:18.671407", "11.03.2024"),  # С точками
])
def test_get_date_different_separators(input_date, expected_output):
    """Тестирование работы с разными разделителями даты"""
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize("invalid_input", [
    "",
    "invalid_date",
    "T02:26:18.671407",
    "2024-03",
    "2024",
    "2024-13-11T02:26:18.671407",
    "2024-03-32T02:26:18.671407",
    "   ",
    "2024-03-11T",
    "2024/03/11",
    "2024-03-11 02:26:18.671407",  # Пробел вместо T
])
def test_get_date_invalid_input(invalid_input):
    """Тестирование обработки некорректных дат"""
    result = get_date(invalid_input)
    assert isinstance(result, str)


def test_get_date_multiple_calls():
    """Тестирование стабильности при многократном вызове"""
    date = "2024-03-11T02:26:18.671407"
    expected = "11.03.2024"
    for _ in range(100):
        assert get_date(date) == expected


def test_get_date_output_format():
    """Тестирование формата выходной строки"""
    result = get_date("2024-03-11T02:26:18.671407")
    parts = result.split(".")
    assert len(parts) == 3
    assert len(parts[0]) in [1, 2]  # День может быть 1 или 2 цифры
    assert len(parts[1]) in [1, 2]  # Месяц может быть 1 или 2 цифры
    assert len(parts[2]) == 4  # Год должен быть из 4 цифр
    # Проверяем, что разделители - точки
    assert result.count(".") == 2


@pytest.mark.parametrize("input_date", [
    "2024-03-11T02:26:18.671407",
    "2024-03-11 02:26:18.671407",
    "2024-03-11 02:26:18",
    "2024-03-11T02:26:18",
])
def test_get_date_various_separators(input_date):
    """Тестирование работы с различными разделителями даты и времени"""
    result = get_date(input_date)
    parts = result.split(".")
    assert len(parts) == 3
    assert len(parts[2]) == 4  # Год должен быть из 4 цифр


@pytest.mark.parametrize("input_date, expected", [
    ("2024-1-1T02:26:18.671407", "1.1.2024"),
    ("2024-01-1T02:26:18.671407", "1.01.2024"),
    ("2024-1-01T02:26:18.671407", "01.1.2024"),
])
def test_get_date_various_digit_counts(input_date, expected):
    """Тестирование дат с разным количеством цифр в дне и месяце"""
    assert get_date(input_date) == expected


def test_get_date_no_time():
    """Тестирование даты без времени"""
    assert get_date("2024-03-11") == "11.03.2024"
    assert get_date("2024-12-31") == "31.12.2024"


def test_get_date_with_timezone():
    """Тестирование даты с часовым поясом"""
    result = get_date("2024-03-11T02:26:18+03:00")
    assert result == "11.03.2024"


def test_get_date_with_spaces():
    """Тестирование даты с пробелами вместо T"""
    assert get_date("2024-03-11 02:26:18.671407") == "11.03.2024"
    assert get_date("2024-03-11 02:26:18") == "11.03.2024"

