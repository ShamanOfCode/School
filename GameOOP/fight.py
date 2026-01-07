import random


def start_fight(player):

    enemy_health = 30 + (player.level - 1) * 10
    enemy_strength = 5 + (player.level - 1) * 2
    print(f"Enemy HP: {enemy_health}, STR: {enemy_strength}")

    while enemy_health > 0 and getattr(player, 'health', 0) > 0:
        action = input("Choose action (attack/flee): ").strip().lower()
        if action == 'attack':
            # player deals damage based on strength
            damage = max(1, getattr(player, 'strength', 5) + random.randint(-2, 4))
            enemy_health -= damage
            print(f"You hit the enemy for {damage} damage. Enemy HP is now {max(0, enemy_health)}.")
        elif action == 'flee':
            # 50% chance to flee successfully
            if random.random() < 0.5:
                print("You fled successfully.")
                return True
            else:
                print("Failed to flee!")
        else:
            print("Invalid action. Choose 'attack' or 'flee'.")
            continue

        # if enemy still alive, it attacks
        if enemy_health > 0:
            edamage = max(1, enemy_strength + random.randint(-3, 2))
            player.health -= edamage
            print(f"Enemy hits you for {edamage}. Your health is now {max(0, player.health)}.")

# Fight information and level up
    if getattr(player, 'health', 0) > 0:
        print("You defeated the enemy!")
        if random.random() < 0.3:
            print("Your level now!")
            player.levelUp()
            player.printStats()
        return True
    else:
        print("You were defeated in battle...")
        return False
