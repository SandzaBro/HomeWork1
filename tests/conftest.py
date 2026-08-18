import pytest


@pytest.fixture
def valid_card():
    return "7000792289606361"


@pytest.fixture
def account_number():
    return "73654108430135874305"


@pytest.fixture
def empty_string():
    return ""
