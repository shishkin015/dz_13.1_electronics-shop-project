import pytest

from src.item import Item


@pytest.fixture(scope="session")
def data_for_test_item():
    instance = Item("Apple", 10, 1)
    return [instance.name, instance.price, instance.quantity], ["Apple", 10, 1]


@pytest.fixture(scope="session")
def data_for_calculate_total_price():
    instance = Item("Apple", 10, 1)
    tested = instance.calculate_total_price()
    expected = instance.price * instance.quantity

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_apply_discount():
    instance = Item("Apple", 10, 1)

    expected = instance.price * 2

    Item.pay_rate = 2
    instance.apply_discount()

    tested = instance.price

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_name_get():
    instance = Item("Apple", 10, 1)
    expected = "Apple"
    tested = instance.name

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_set_name():
    instance = Item("Apple", 10, 1)
    instance.name = "Aaappppplllleee"

    tested = instance.name
    expected = "Aaapppppll"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_string_to_number():
    instance = Item("Apple", 10, 1)
    tested = instance.string_to_number("10")
    expected = 100

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_instantiate_from_csv():
    Item.instantiate_from_csv()

    expected = "Смартфон"
    tested = Item.all[0].name

    return tested, expected