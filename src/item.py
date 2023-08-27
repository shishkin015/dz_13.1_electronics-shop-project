import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        """
        Getter Возвращает название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Setter Изменяет название товара если название больше 10 символов.

        :param value: Название товара.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создание экземпляра класса item из файла csv.
        """
        cls.all = []
        with open('../src/items.csv') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for row in csv_dict:
                Item(str(row['name']), float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string: str) -> int:
        return int(float(string))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'
