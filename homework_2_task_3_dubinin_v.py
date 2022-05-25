"""
Task_3
Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию о товаре.
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
    def get_parent_data(self):
        return f'{self.name}: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Chevrolet', 10000)
    print(product.get_parent_data())
    product.price = 12500
    print(product.get_parent_data())
