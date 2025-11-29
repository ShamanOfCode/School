# Pick your route so maybe it will random ask if you want to go through a forest or a cave or a mountain
# Random event is a treasure chest or a trap
# or also enemy encounter
# TODO: Left, Right, Straight, Back options for movement

import random

class World:
    def __init__(self):
        self.locations = ["forest", "cave", "mountain"]
        self.events = ["treasure chest", "trap", "enemy encounter"]

    def choose_location(self):
        location = random.choice(self.locations)
        print(f"You have chosen to go through the {location}.")
        return location

    def trigger_event(self):
        event = random.choice(self.events)
        print(f"As you proceed, you encounter a {event}!")
        return event
    def handle_event(self, event, hero, enemy):
        if event == "treasure chest":
            loot = random.randint(10, 50)
            hero.health += loot
            print(f"You found a treasure chest and gained {loot} health!")
        elif event == "trap":
            damage = random.randint(5, 20)
            hero.health -= damage
            print(f"You fell into a trap and lost {damage} health!")
        elif event == "enemy encounter":
            print("An enemy appears!")
            while hero.is_alive() and enemy.is_alive():
                hero.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(hero)
                print(f"{hero.name} Health: {hero.health}, {enemy.name} Health: {enemy.health}")
            if hero.is_alive():
                print(f"{hero.name} has defeated the {enemy.name}!")
            else:
                print(f"{hero.name} has been defeated by the {enemy.name}!")


class Book:
    """Simple book object with a title and numeric priority."""
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    def __repr__(self):
        return f"Book(title={self.title!r}, priority={self.priority})"


def bubble_sort_books(books, reverse=False):
    """
    Sorts a list of book-like objects (objects with .priority attribute or dicts with 'priority') in place
    using bubble sort. Returns the same list for convenience.

    Parameters:
    - books: list of objects or dicts containing a numeric 'priority'
    - reverse: if True, sort descending (highest priority first). Default False (ascending).
    """
    n = len(books)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # extract priority for left and right elements
            left = books[j]
            right = books[j + 1]
            a = getattr(left, 'priority', None) if not isinstance(left, dict) else left.get('priority')
            b = getattr(right, 'priority', None) if not isinstance(right, dict) else right.get('priority')

            if a is None or b is None:
                # If priority missing, treat as lowest priority (None -> -inf)
                a_val = float('-inf') if a is None else a
                b_val = float('-inf') if b is None else b
            else:
                a_val = a
                b_val = b

            # Decide whether to swap depending on reverse flag
            should_swap = (a_val < b_val) if reverse else (a_val > b_val)
            if should_swap:
                books[j], books[j + 1] = books[j + 1], books[j]
                swapped = True
        if not swapped:
            break
    return books
