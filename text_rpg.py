# A simple text-based RPG game in Python

import random

class Character:
    def __init__(self, name, hp, attack_min, attack_max):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        damage = random.randint(self.attack_min, self.attack_max)
        other.hp -= damage
        return damage

def main():
    hero = Character("Hero", hp=30, attack_min=4, attack_max=8)
    goblin = Character("Goblin", hp=20, attack_min=2, attack_max=6)

    print("A wild Goblin appears!")

    while hero.is_alive() and goblin.is_alive():
        print(f"\n{hero.name} HP: {hero.hp} | {goblin.name} HP: {goblin.hp}")
        action = input("Do you [a]ttack or [r]un? ").strip().lower()
        if action == 'a':
            dmg = hero.attack(goblin)
            print(f"You strike the Goblin for {dmg} damage.")
            if not goblin.is_alive():
                print("The Goblin has been defeated! You win!")
                break
            dmg = goblin.attack(hero)
            print(f"The Goblin hits you for {dmg} damage.")
            if not hero.is_alive():
                print("You have been defeated. Game over.")
                break
        elif action == 'r':
            print("You run away from the battle!")
            break
        else:
            print("Invalid action. Choose 'a' to attack or 'r' to run.")

if __name__ == "__main__":
    main()
