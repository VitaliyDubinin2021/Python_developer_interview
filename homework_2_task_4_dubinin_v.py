"""
Task_4
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
"""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.__discount = discount

    def __str__(self):
        return f'{self.name} со скидкой: {self.price * (1 - self.__discount / 100)}'

    @property
    def discount(self):
        return self.__discount

    def get_parent_data(self):
        return f'{self.name}: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Chevrolet', 10000, 10)
    print(product.get_parent_data())
    product.price = 1500
    print(product.get_parent_data())
    print(product)