"""
Character Attributes
Standard: HEALTH, MANA, STRENGTH, AGILITY
W = Warrior: More HEALTH and STRENGTH, less MANA
M = Mage: More MANA, less HEALTH and STRENGTH
S = Spellblade: Balanced HEALTH, MANA, STRENGTH
"""
class Character:
    def __init__(self, name, playerClass):
        self.name = name
        self.playerClass = playerClass
        self.level = 1
        self.classSelection(playerClass)

    def classSelection(self, playerClass):
        if playerClass == 'W': # Warrior
            self.health = 150
            self.mana = 50
            self.strength = 15
        elif playerClass == 'M': # Mage
            self.health = 100
            self.mana = 150
            self.strength = 5
        elif playerClass == 'S': # Spellblade
            self.health = 120
            self.mana = 100
            self.strength = 10
        else:
            # calling error and returning to start when user enters something different then expected
            print("Invalid entry")
            return

    def levelUp(self):
        # if elif else for different class levelup stats
        self.level += 1
        if self.playerClass == 'W': # Warrior
            self.health += 50
            self.mana += 10
            self.strength += 10
        elif self.playerClass == 'M': # Mage
            self.health += 20
            self.mana += 80
            self.strength += 3
        elif self.playerClass == 'S': # Spellblade
            self.health += 30
            self.mana += 50
            self.strength += 5

    def printStats(self):
        print("Your current stats are:")
        print(f"Name: {self.name}")
        print(f"Class: {self.playerClass}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Strength: {self.strength}")