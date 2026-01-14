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
        # cached available directions for the current location
        self._available = None
        self._available_location = None
        # lower encounter chance so fights are less frequent
        self.encounter_chance = 0.4

    def _compute_available_for_current(self):
        possible = ['left', 'forward', 'right']
        available = [d for d in possible if random.random() > 0.35]
        if not available:
            available = [random.choice(possible)]
        return available

    def start(self, player):
        # Choose your path and world start
        print(f"\nEntering the world, {player.name}! Type 'quit' at the hub to leave the game.")

        while True:
            # HUB
            print('\nWhere would you like to go?')
            print('Locations: ' + ', '.join([loc.capitalize() for loc in self.locations]))
            dest = input("Enter location: ").strip().lower()
            # allow quitting from the hub
            if dest == 'quit':
                print('Goodbye! Exiting the world.')
                return
            if dest not in self.locations:
                print('Unknown location. Choose again.')
                continue

            # Enter the chosen location
            self.current = dest
            # compute and cache available for this location (won't change until move)
            self._available = self._compute_available_for_current()
            self._available_location = self.current

            print(f"\nYou travel to the {self.current.capitalize()}.")

            # LOCATION loop: stay until user types 'exit' to return to hub or player dies
            while True:
                print(f"\nYou are at the {self.current.capitalize()}.")

                # use the cached available for this location (do NOT recompute here)
                available = list(self._available)
                possible = ['left', 'forward', 'right']

                print("Available directions:", ', '.join(available))
                print("Type a direction to move, or 'exit' to return to the hub.")

                # Keep prompting without recomputing `available` until a valid action is taken
                should_return_to_hub = False
                while True:
                    choice = input("Where do you want to go? ").strip().lower()
                    if choice == 'exit':
                        print('Returning to the hub...')
                        should_return_to_hub = True
                        break

                    if choice not in possible:
                        print("Invalid direction. Try again.")
                        # re-show the same available directions so they don't appear to change
                        print("Available directions:", ', '.join(available))
                        continue

                    if choice not in available:
                        print("That way is blocked. Choose a different direction.")
                        # re-show the same available directions so they don't appear to change
                        print("Available directions:", ', '.join(available))
                        continue

                    # valid and available
                    break

                if should_return_to_hub:
                    break  # go back to hub loop

                # move to new location based on the chosen direction
                new_location = self.map[self.current][choice]
                print(f"You move {choice} and arrive at the {new_location.capitalize()}.")

                # update current location and compute availability for the new location immediately
                self.current = new_location
                self._available = self._compute_available_for_current()
                self._available_location = self.current

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
