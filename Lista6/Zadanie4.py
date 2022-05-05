from Lista6.Zadanie1 import ControlledText


class Ident_number(ControlledText):

    def __init__(self, number):
        super().__init__(str(number))

        number_str = str(number)
        sum = 0
        for i in number_str[:7]:
            sum += int(i)

        last_int_expected = '0' + str(sum % 97)
        last_int = (number_str[len(number_str) - 2: len(number_str)])

        if isinstance(number, int) and len(str(number)) == 9 and last_int == last_int_expected:
            self.text = str(number)

        else:
            raise ValueError("wrong number")

    @property
    def number(self):
        print('Getting...')
        return self.text

    @number.setter
    def number(self, value):
        raise ValueError('You cant change value')


# num = Ident_number(111111107)
# num.number = 234235234
