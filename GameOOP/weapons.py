# TODO: Different type of weapons for specific hero class only like long sword only for barbar
import random

class Weapon:
    """Base class for weapons."""
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"Weapon(name={self.name!r}, damage={self.damage})"

class Sword(Weapon):
    """Sword weapon."""
    def __init__(self):
        super().__init__("Sword", random.randint(15, 25))

class Bow(Weapon):
    """Bow weapon."""
    def __init__(self):
        super().__init__("Bow", random.randint(10, 20))

class Staff(Weapon):
    """Staff weapon."""
    def __init__(self):
        super().__init__("Staff", random.randint(5, 15))
class Dagger(Weapon):

    def __init__(self):
        super().__init__("Dagger", random.randint(8, 18))
class Axe(Weapon):

    def __init__(self):
        super().__init__("Axe", random.randint(20, 30))
class Mace(Weapon):
    def __init__(self):
        super().__init__("Mace", random.randint(18, 28))