import json
import random


class Character:
    def __init__(self, name: str, health: int, attackname: str, attackdamage: int):
        self.name = name
        self.health = health
        self.attackname = attackname
        self.attackdamage = attackdamage


def attack(attacker:Character, target: Character):
    if (random.randint(0,1)) == 1:
        attackeffect = random.random(0.0, 1.1)
        damage = attacker.attackdamage * attackeffect
        target.health -= damage
        print(f'{attacker.name.title()} used {attacker.attackname}! It caused {damage} damage.') # update display of target's hp
    else:
        print(f'{attacker.name.title()} missed!')
