from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def number_of_sim(self, value):
        if value <= 0 or not isinstance(value, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

        self.number_of_sim = value

    def __add__(self, other):
        if isinstance(other, Item) or issubclass(other.__class__, Phone):
            return self.quantity + other.quantity

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"
