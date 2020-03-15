from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, input_param):
        self.param = input_param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return 2 * self.param + 0.3


coat_size = int(input("Введите размер пальто: "))
costume_height = int(input("Введите рост, на который надо пошить костюм: "))
coat = Coat(coat_size)
costume = Costume(costume_height)
print(f"Затраты на пошив пальто: {coat.consumption}")
print(f"Затраты на пошив костюма: {costume.consumption}")
print(f"Суммарный расход ткани: {coat.consumption + costume.consumption}")
