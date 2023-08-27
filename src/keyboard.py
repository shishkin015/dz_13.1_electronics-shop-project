from src.item import Item


class MixinKeyboard:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self

    def language(self, value):
        if value in None:
            return self.language
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    print(str(kb.language))

