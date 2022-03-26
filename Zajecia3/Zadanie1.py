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

    def set_i1(self, i1):
        if isinstance(i1, (int, float)):
            self.i1 = i1
        else:
            raise TypeError('The price must be of type int or float')


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
