import pytest


@pytest.fixture
def valid_card() -> str:
    """Фикстура с корректным номером карты"""
    return "7000792289606361"


@pytest.fixture
def account_number() -> str:
    """Фикстура с корректным номером счета"""
    return "73654108430135874305"
