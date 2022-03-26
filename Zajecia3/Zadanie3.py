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


monster1 = Monster("Ork", 60, 30, "right", 100)
monster2 = Monster("Goblin", 40, 40, "left", 120)

is_not_end = True

while is_not_end:
    monster1.fight(monster2)
    monster2.fight(monster1)
    monster1.movement()
    monster2.movement()
    monster1.heal()
    if monster1.health < 0:
        print("Monster " + monster2.name + " won")
        is_not_end = False
    elif monster2.health < 0:
        print("Monster " + monster1.name + " won")
        is_not_end = False



