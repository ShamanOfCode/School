import character
import world
import fight
import random


def main():
    # Custom Character creation
    player = input("Enter your character's name: ")
    playerClass = input("Select class:\n(W)arrior\n(M)age\n(S)pellblade\n").upper()

    p = character.Character(player, playerClass)
    p.printStats()

    # Start the world loop
    w = world.World()
    w.start(p)


if __name__ == '__main__':
    main()
