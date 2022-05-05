from Lista6.Zadanie1 import ControlledText


class FirstName(ControlledText):
    names = []
    file = 'PopularneImiona.txt'

    def get_popular_names(self):
        with open(FirstName.file, 'r', encoding='utf-8') as f:
            for line in f:
                FirstName.names.append(line.strip())

    def __init__(self, name):
        super().__init__(name)

        if not FirstName.names:
            self.get_popular_names()

        self.name = name

    @property
    def name(self):
        return self.text

    @name.setter
    def name(self, value):
        if value in FirstName.names:
            self.text = value.capitalize()
        else:
            raise ValueError("Name is not known")

    @name.deleter
    def name(self):
        del self.text

    @staticmethod
    def male_name(new_name):
        if new_name[-1] != 'a':
            return True
        else:
            return False

    @staticmethod
    def female_name(new_name):
        if new_name[-1] == 'a':
            return True
        else:
            return False

    def is_female(self):
        return self.female_name(self.text)

    def is_male(self):
        return self.male_name(self.text)


# ob = FirstName("  ")
# print(ob.name)
# ob.name = "Lena"
# print(ob.name)
# ob.name = "Hellena"
# print(ob.is_male())
# print(ob.is_female())
