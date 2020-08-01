class Product:
    def __init__(self, price):
        self.__price = price

    @propertyX
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
           raise ValueError("Price cannot be negative!")
        self.__price = value

product = Product(50)
product.price = 20