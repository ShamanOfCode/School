import world

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, hero):
        hero.health -= self.attack_power
        print(f"{self.name} attacks {hero.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0


def main():
    # Create world, hero and an enemy
    world_obj = world.World()
    hero = Hero("Hero", 100, 20)
    enemy = Enemy("Goblin", 50, 10)

    # Use the world to pick a location and trigger an event
    world_obj.choose_location()
    event = world_obj.trigger_event()

    # Let the world handle the event (it will run combat if it's an enemy encounter)
    world_obj.handle_event(event, hero, enemy)

    # If the event wasn't an enemy encounter, run a normal combat afterwards if both are alive
    if event != "enemy encounter" and hero.is_alive() and enemy.is_alive():
        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            print(f"{hero.name} Health: {hero.health}, {enemy.name} Health: {enemy.health}")

        if hero.is_alive():
            print(f"{hero.name} has defeated the {enemy.name}!")
        else:
            print(f"{hero.name} has been defeated by the {enemy.name}!")


if __name__ == "__main__":
    main()
