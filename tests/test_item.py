"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError


@pytest.fixture
def item():
    """Фикстура для создания объекта класса Item."""
    return Item(name='test_name1111', price=1.5, quantity=10)


def test_item_init(item):
    """Тест для создания объекта класса Item."""
    assert item.name == 'test_name1111'
    assert item.price == 1.5
    assert item.quantity == 10
    assert item.name == str(item)
    assert item.price == float(item.price)
    assert item.quantity == int(item.quantity)


def test_item_calculate_total_price(item):
    """Тест для расчёта стоимости товара."""
    assert item.calculate_total_price() == 15.0


def test_item_apply_discount(item):
    """Тест для применения скидки к стоимости товара."""
    item.apply_discount()
    assert 1.5 * Item.pay_rate == item.price
    assert item.price == 1.5


def test_item_repr(item):
    """Тест для вывода информации о товаре."""
    assert repr(item) == "Item('test_name1111', 1.5, 10)"


def test_item_str(item):
    """Тест для вывода информации о товаре."""
    assert str(item) == "test_name1111"


def test_instantiate_from_csv_error():
    """Проверяем присутствие или повреждение file.csv"""
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv('')

    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv('test_csv.csv')
