"""
A class used to represent an animal
"""
class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    """get the name of the animal
    :return: the name of the animal
    :rtype: str
    """
    def get_name(self):
        return self._name
    """check if the animal is hungry
    :return: True if the animal is hungry, False otherwise
    :rtype: bool
    """
    def is_hungry(self):
        return self._hunger > 0
    """drop the hunger level by one.
    :rtype None
    """
    def feed(self):
        if (self._hunger > 0):
            self._hunger -= 1

    def talk(self): pass

"""
A class used to represent a Dog that inherits animal
"""
class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self) -> str:
        return "Dog " + self._name

    def talk(self):
        return "woof woof"

    def fetch_stick(self):
        print("There you go, sir!")

"""
A class used to represent a Cat that inherits animal
"""
class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self) -> str:
        return "Cat " + self._name

    def talk(self):
        return "meow"

    def chase_laser(self):
        print("Meeeeow")

"""
A class used to represent a Skunk that inherits animal
"""
class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def __str__(self) -> str:
        return "Skunk " + self._name

    def talk(self):
        return "tsssss"

    def stink(self):
        print("Dear lord!")

"""
A class used to represent a Unicorn that inherits animal
"""
class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self) -> str:
        return "Unicorn " + self._name

    def talk(self):
        return "Good day, darling"

    def sing(self):
        print("I’m not your toy...")

"""
A class used to represent a Dragon that inherits animal
"""
class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def __str__(self) -> str:
        return "Dragon " + self._name

    def talk(self):
        return "Raaaawr"

    def breath_fire(self):
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("Mcfly", 80)

    zoo_lst = [brownie, zelda, stinky, keith, lizzy,
               doggo, kitty, stinky_jr, clair, mcfly]
    for animal in zoo_lst:
        print(animal)
        while animal.is_hungry():
            animal.feed()
        print(animal.talk())
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
