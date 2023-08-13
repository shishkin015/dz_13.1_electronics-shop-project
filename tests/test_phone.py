import pytest

from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 4, 2)


def test_phone_init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 4
    assert phone.number_of_sim == 2
    assert phone.name == str(phone)
    assert phone.price == float(phone.price)
    assert phone.quantity == int(phone.quantity)
    assert phone.number_of_sim == int(phone.number_of_sim)


def test_phone_add(phone):
    phone1 = Phone("iPhone 14", 120_000, 4, 2)
    phone2 = Phone("iPhone 14", 120_000, 4, 2)

    assert phone1.__add__(phone2) == 8


def test_phone_number_of_sim(phone):
    phone = Phone("iPhone 14", 120_000, 4, 0)
    assert phone.number_of_sim == 0


def test_phone_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 4, 2)"


def test_phone_str(phone):
    assert str(phone) == "iPhone 14"

