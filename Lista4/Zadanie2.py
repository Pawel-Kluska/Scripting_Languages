class Calculator:
    __profit = 0.3
    _euro = 4.74
    _usd = 4.31

    def __init__(self, price):
        self.price = price

    def get_margin(self):
        return self.price * Calculator.__profit + self.price

    def get_USD(self):
        return self.price / Calculator._usd

    def get_EURO(self):
        return self.price / Calculator._euro

    def get_margin_USD(self):
        return self.get_margin() / Calculator._usd

    def get_margin_EURO(self):
        return self.get_margin() / Calculator._euro

    @property
    def price(self):
        print('Getting...')
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise TypeError('The price attribute must be positive.')
        else:
            raise ValueError('The price attribute must be an int or float value.')

    @price.deleter
    def price(self):
        del self._price


list_of_products = [Calculator(120), Calculator(400), Calculator(1000)]

for i in list_of_products:
    print(i.get_margin())
    print(i.get_USD())
    print(i.get_margin_EURO())


cal = Calculator(150)
cal.price = 900
print(cal.price)
cal.price = -4

