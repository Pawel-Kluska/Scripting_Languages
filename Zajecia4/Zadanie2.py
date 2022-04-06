class Animal:

    def __init__(self, sound, size):
        self._sound = sound
        self._size = size

    def makeSound(self):
        pass


class Dog(Animal):

    def __init__(self, weight, size, *args):
        super().__init__(weight, size)
        self._list_of_favourite_bones = args

    def makeSound(self):
        print("Hau hau")

    def getBones(self):
        return self._list_of_favourite_bones

    def giveBone(self, bone):
        if bone in self._list_of_favourite_bones:
            print("feeded")
        else:
            print("dog doesn't like this bone")

    def __len__(self):
        return len(self._list_of_favourite_bones)


class Cat(Animal):

    def __init__(self, weight, size, **kwargs):
        super().__init__(weight, size)
        self._dict_of_favourite_food_price = kwargs

    def makeSound(self):
        print("Miauuuu")

    def getFood(self):
        return self._dict_of_favourite_food_price

    def giveFood(self, food, price):
        if food in self._dict_of_favourite_food_price:
            if self._dict_of_favourite_food_price[food] < price:
                print("feeded")
        else:
            print("Wrong food")

    def __len__(self):
        return len(self._dict_of_favourite_food_price)


class Hamster(Animal):

    def __init__(self, weight, size, condition):
        super().__init__(weight, size)
        self._condition = condition

    def makeSound(self):
        print("Biiiiip ")

    def chceckCondition(self):
        if self._condition > 10:
            print("Hamster has good condition")
        else:
            print("Hamseter is exhausted")



h = Hamster(20, 10, "Good")
cat = Cat(3, 4, food1=10, food2=15, food3=20)
print(len(cat))

cat.giveFood("food5", 30)

d = Dog(20, 30,"bone1", "bone2", "bone3", "bone4")
print(len(d))

a = Animal(30, 59)
h.makeSound()
cat.makeSound()



