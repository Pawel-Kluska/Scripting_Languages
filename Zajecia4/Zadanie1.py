class Stwor:

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

    def __repr__(self):
        return "name = {}, force = {}, defence = {}, position = {}, health = {}"\
            .format(self.name, self.force, self.defence, self.position, self.health)


class Czlowiek(Stwor):
    def __init__(self, name, force, defence, position, health):
        super().__init__(name, force, defence, position, health)

    def callSoliders(self):
        self.force += 10
        self.defence += 10


class Zwierze(Stwor):
    def __init__(self, name, force, defence, position, health, size):
        super().__init__(name, force, defence, position, health)
        self.size = size


class Potwor(Stwor):
    def __init__(self, name, force, defence, position, health, condition):
        super().__init__(name, force, defence, position, health)
        self.condition = condition


class Lucznik(Czlowiek):
    def __init__(self, name, force, defence, position, health, arrows):
        super().__init__(name, force, defence, position, health)

    def fight(self, other_monster):

        if self.force < other_monster.defence:
            other_monster.health -= 0.8 * self.force

        if self.arrows > 0:
            other_monster.health -= 5
            self.arrows -= 1

        else:
            other_monster.health -= self.force


class Czarodziej(Czlowiek):
    def __init__(self, name, force, defence, position, health, mana):
        super().__init__(name, force, defence, position, health)
        self.mana = mana

    def heal(self):
        self.health += 20


class Wilkolak(Czlowiek):
    def __init__(self, name, force, defence, position, health, isChanged):
        super().__init__(name, force, defence, position, health)
        self.isChanged = isChanged

    def fight(self, other_monster):

        if self.isChanged:
            self.force += 20

        if self.force < other_monster.defence:
            other_monster.health -= 0.8 * self.force

        else:
            other_monster.health -= self.force


wilkolak = Wilkolak("Wilkolak", 100, 50, "left", 100, True)
print(issubclass(Wilkolak, Czlowiek))
print(issubclass(Czlowiek, Stwor))
print(issubclass(Lucznik, Potwor))

print(repr(wilkolak))
wilkolak.callSoliders()
print(repr(wilkolak))

czarodziej = Czarodziej("Czarodziej", 100, 50, "left", 100, 100)
czarodziej.heal()
print(str(czarodziej.__class__.__name__) + " Zdrowie " + str(czarodziej.health))

stwor = Stwor("Stwor", 100, 50, "left", 100)
stwor.heal()
print(str(stwor.__class__.__name__) + " Zdrowie " + str(stwor.health))
