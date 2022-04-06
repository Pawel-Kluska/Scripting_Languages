class Z1:
    atr1 = "atr1"
    atr2 = 2
    atr3 = 3.3

    def __init__(self):
        self.i1 = 11
        self.i2 = "i2"
        self.i3 = 33

    def display_attrs(self):
        for attr in self.__dict__.values():
            print(attr)

    @property
    def i1(self):
        return self._i1

    @i1.setter
    def i1(self, value):
        if isinstance(value, int):
            self._i1 = value

    @i1.deleter
    def i1(self):
        del self._i1


list_of_objects = []

for i in range(3):
    list_of_objects.append(Z1())

for i in range(3):
    print(Z1.__dict__)

setattr(list_of_objects[0], 'material', 'iron')
setattr(list_of_objects[1], 'material', 'wood')
setattr(list_of_objects[2], 'material', 'steel')

for i in list_of_objects:
    print(i.__dict__)

list_of_objects[0].display_attrs()

obj = Z1()
obj.i1 = 8

print(obj.i1)



