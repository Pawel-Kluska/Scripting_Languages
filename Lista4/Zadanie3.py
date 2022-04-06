class Monster:

    def __init__(self, name, force, defence, position, health):
        self.name = name
        self.force = force
        self.defence = defence
        self.position = position
        self.health = health

    def fight(self, other_monster):

        if self.force < other_monster.defence:
            other_monster.health -= 0.8 * self.force

        else:
            other_monster.health -= self.force


    def movement(self):
        if self.position == "left":
            self.position = "right"
        else:
            self.position = "right"


    def heal(self):
        self.health += 10

class Game:
    level = 0

    def __init__(self, monster1, monster2):
        Game.level += 1
        self.monster1 = monster1
        self.monster2 = monster2

    def play(self):
        is_not_end = True

        while is_not_end:
            self.monster1.fight(self.monster2)
            self.monster2.fight(self.monster1)
            self.monster1.movement()
            self.monster2.movement()
            self.monster1.heal()
            if self.monster1.health < 0:
                print("Monster " + self.monster2.name + " won")
                is_not_end = False
            elif self.monster2.health < 0:
                print("Monster " + self.monster1.name + " won")
                is_not_end = False

    @property
    def monster1(self):
        return self._monster1

    @monster1.setter
    def monster1(self, value):
        if isinstance(value, Monster):
            self._monster1 = value
        else:
            raise ValueError('Monster required')

    @monster1.deleter
    def monster1(self):
        del self._monster1

    @property
    def monster2(self):
        return self._monster2

    @monster2.setter
    def monster2(self, value):
        if isinstance(value, Monster):
            self._monster2 = value
        else:
            raise ValueError('Monster required')

    @monster2.deleter
    def monster2(self):
        del self._monster2


m1 = Monster("Ork", 60, 30, "right", 100)
m2 = Monster("Goblin", 40, 40, "left", 120)

game = Game(m1, m2)
game.play()

game.monster2 = Monster("Dwaff", 100, 100, "left", 120)
game.play()





