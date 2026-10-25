import json
import random
from bookdatabase import isbn_database, char_database

# builds Character class
class Character:
    def __init__(self, name: str, health: int, attackname: str, attackdamage: int):
        self.name = name
        self.health = health
        self.attackname = attackname
        self.attackdamage = attackdamage

    
    def char_to_dict(self):
        return {
            "Name": self.name,
            "Health": self.health,
            "Attack": self.attackname,
            "AttackDamage": self.attackdamage
        }



# attack function that randomly generates whether attack lands or not and effectiveness of attack, prints results
def attack(attacker:Character, target: Character):
    if (random.randint(0,1)) == 1:
        attackeffect = random.uniform(0.0, 1.5)
        damage = attacker.attackdamage * attackeffect
        target.health -= damage
        x = attacker
        print(f'{attacker.name.title()} used {attacker.attackname}! It caused {damage} damage.') # update display of target's hp
        return x
    else:
        print(f'{attacker.name.title()} missed!')

# builds Character class from given isbn code
def get_char(isbn):
    # retrieves character from book (assumes there is one character per book right now). If a character doesn't exist, return "Invalid"
    char = isbn_database.get(isbn, "Invalid")

    if (char == "Invalid"):
        return "Invalid"
    
    chartraits = char_database[char]
    
    return Character(char, chartraits[0], chartraits[1], chartraits[2])

# returns a random character
def random_char():
    char = random.choice(list(char_database.keys()))
    chartraits = char_database[char]
    return Character(char, chartraits[0], chartraits[1], chartraits[2])

# creates Character classes, one for computer, one for playable character
def solo_gamesetup(isbn):
    computer_char = random.choice(list(char_database.keys()))
    computer = Character(computer_char, char_database[computer_char][0], char_database[computer_char][1], char_database[computer_char][2])

    player = get_char(isbn)

    return computer, player

#creates Character classes for two playable characters
#def multi_gamesetup(isbn):
 #   return get_char(isbn[0]), get_char(isbn[1])



def main(isbn):
    p1, p2 = solo_gamesetup(isbn)
    turn = random.randint(0,1)

    #swaps turns between players while both players have health
    while p1.health > 0 and p2.health > 0:
        if turn == 0:
            attack(p1, p2)
            turn+=1
        else:
            attack(p2, p1)
            turn-=1
            