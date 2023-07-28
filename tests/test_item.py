"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    """Фикстура для создания объекта класса Item."""
    return Item(name='test_name1111', price=1.5, quantity=10)


def test_item_init(item):
    """Тест для создания объекта класса Item."""
    assert item.name == 'test_name1111'
    assert item.price == 1.5
    assert item.quantity == 10


def test_item_calculate_total_price(item):
    """Тест для расчёта стоимости товара."""
    assert item.calculate_total_price() == 15.0


def test_item_apply_discount(item):
    """Тест для применения скидки к стоимости товара."""
    item.apply_discount()
    assert 1.5 * Item.pay_rate == item.price
    assert item.price == 1.5




