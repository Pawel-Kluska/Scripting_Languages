from Zadanie4 import Ident_number
from Zadanie2 import FirstName
from Zadanie3 import LastName


class Person:

    def __init__(self, *args):
        if len(args) == 3:
            if isinstance(args[0], Ident_number) and isinstance(args[1], FirstName) and isinstance(args[2], LastName):
                self.first_name_obj = args[0]
                self.last_name_obj = args[1]
                self.number_obj = args[2]
            else:
                raise ValueError("Wrong classes added")
        elif len(args) == 1:
            self.fromString(args[0])
        else:
            raise ValueError("Wrong number of parameters")

    @classmethod
    def from_string_constructor(cls, text):
        person = cls.fromString(text)
        return person

    def fromString(self, controlled_text_string):
        texts = controlled_text_string.split(sep='/')

        number_object = Ident_number(int(texts[0]))
        first_name_object = FirstName(texts[1])
        last_name_object = LastName(texts[2])

        return Person(number_object, first_name_object, last_name_object)


nr = Ident_number(111111107)
f_name = FirstName('Jan')
l_name = LastName('Kowalski')

p1 = Person(nr, f_name, l_name)
p2 = Person("111111107/Jan/Kowalski")
p1.fromString('111111107/Jan/Kowalski')

print('{}{}{}'.format(p1.number_obj, p1.last_name_obj, p1.first_name_obj))
