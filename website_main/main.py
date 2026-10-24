import json
import random
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

def get_isbn(image):
    img = Image.open(image)
    array = decode(img, symbols=[ZBarSymbol.EAN13])
    isbnarray = []
    for code in array:
        isbnarray.append(code.data.decode("utf-8"))
    return isbnarray

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