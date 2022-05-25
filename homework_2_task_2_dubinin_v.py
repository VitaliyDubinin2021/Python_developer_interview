"""
Task_2
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей логики
работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом, чтобы получить
доступ к защищенным переменным.
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

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name}: {self.price}'

if __name__ == '__main__':
    product = ItemDiscountReport('Chevrolet', 10000)
    print(product.get_parent_data())




