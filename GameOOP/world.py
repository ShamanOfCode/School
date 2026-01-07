import random
import fight


class World:
    def __init__(self):
        # four named locations
        self.locations = ['castle', 'forest', 'village', 'lake']
        # map: from each location, where each direction leads
        self.map = {
            'castle': {'left': 'forest', 'forward': 'village', 'right': 'lake'},
            'forest': {'left': 'lake', 'forward': 'castle', 'right': 'village'},
            'village': {'left': 'castle', 'forward': 'lake', 'right': 'forest'},
            'lake': {'left': 'village', 'forward': 'forest', 'right': 'castle'},
        }
        self.current = 'castle'
        # lower encounter chance so fights are less frequent
        self.encounter_chance = 0.4

    def start(self, player):
        # Choose your path and world start
        print(f"\nEntering the world, {player.name}! Type 'quit' at the hub to leave the game.")

        while True:
            # HUB
            print('\nWhere would you like to go?')
            print('Locations: ' + ', '.join([loc.capitalize() for loc in self.locations]))
            dest = input("Enter location: ").strip().lower()
            if dest not in self.locations:
                print('Unknown location. Choose again.')
                continue

            # Enter the chosen location
            self.current = dest
            print(f"\nYou travel to the {self.current.capitalize()}.")

            # LOCATION loop: stay until user types 'exit' to return to hub or player dies
            while True:
                print(f"\nYou are at the {self.current.capitalize()}.")

                possible = ['left', 'forward', 'right']
                # 35% chance of blocked road
                available = [d for d in possible if random.random() > 0.35]
                if not available:
                    available = [random.choice(possible)]

                print("Available directions:", ', '.join(available))
                print("Type a direction to move, or 'exit' to return to the hub.")

                choice = input("Where do you want to go? ").strip().lower()
                if choice == 'exit':
                    print('Returning to the hub...')
                    break  # go back to hub loop

                if choice not in possible:
                    print("Invalid direction. Try again.")
                    continue

                if choice not in available:
                    print("That way is blocked. Choose a different direction.")
                    continue

                new_location = self.map[self.current][choice]
                print(f"You move {choice} and arrive at the {new_location.capitalize()}.")
                self.current = new_location

                # encounter chance
                if random.random() < self.encounter_chance:
                    print("A hostile creature appears!")
                    survived = fight.start_fight(player)
                    if not survived:
                        if getattr(player, 'health', 0) <= 0:
                            print('You have no health left. Exiting world.')
                            return
                        else:
                            print("You survived")
                else:
                    print("The area is peaceful")
