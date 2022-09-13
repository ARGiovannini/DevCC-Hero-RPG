import random
from Characters import my_hero
from Characters import Villain_1
from Characters import villain_2
from Characters import villain_3

def battle(villain):
    while my_hero['health'] > 0:
        my_attack = random.choice(my_hero['attack'])
        villain['health'] -= my_attack[1]
        if villain['health'] <= 0:
            print(f"{my_hero['name']} has defeated {villain['name']}!")
            print("")
            break
        else:
            print(f"{my_hero['name']} attacked with a {my_attack[0]} causing {my_attack[1]} HP of damage. {villain['name']} has {villain['health']} health left.")
            print("")
        villain_attack = random.choice(villain['attack'])
        my_hero['health'] -= villain_attack[1]
        if my_hero['health'] <= 0:
            print("You have died")
            break
        else:
            print(f"{villain['name']} attacked with a {villain_attack[0]} causing {villain_attack[1]} HP of damage. {my_hero['name']} has {my_hero['health']} health left.")
            print("")

print("")
print(f"{my_hero['name']}, you wield the triforce of courage. \nYou must embark on a quest to defeat Gannon, who holds the triforce of power, \nand rescue princess zelda, who holds the triforce of wisdom.")
print("")
print(f"{my_hero['name']} has traveled to fire mountain and encountered {Villain_1['name']} (Level: {Villain_1['level']} Health: {Villain_1['health']})")
print("")
battle(Villain_1)
battle(villain_2)
battle(villain_3)
