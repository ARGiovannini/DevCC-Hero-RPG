import random
from Characters import my_hero
from Characters import villain_1
from Characters import villain_2
from Characters import villain_3

def add_inventory(villain):
    my_hero['equipment'].update(villain['equipment'])
    for inventory_item in villain['equipment']:
        print(f"+ {inventory_item} added to {my_hero['name']}'s inventory.")
        print("")


def battle(villain):
    while my_hero['health'] > 0:
        my_attack = random.choice(my_hero['attacks'])
        villain['health'] -= my_attack[1]
        if villain['health'] <= 0:
            print(f"{my_hero['name']} has defeated {villain['name']}!")
            print("")
            add_inventory(villain)
            break
        else:
            print(f"{my_hero['name']} attacked with a {my_attack[0]} causing {my_attack[1]} HP of damage. {villain['name']} has {villain['health']} health left.")
            print("")
        villain_attack = random.choice(villain['attacks'])
        my_hero['health'] -= villain_attack[1]
        if my_hero['health'] <= 0:
            print("You have died")
            break
        else:
            print(f"{villain['name']} attacked with a {villain_attack[0]} causing {villain_attack[1]} HP of damage. {my_hero['name']} has {my_hero['health']} health left.")
            print("")

def run_game():
    print("")
    print(f"{my_hero['name']}, you wield the triforce of courage. \nYou must embark on a quest to defeat Gannon, who holds the triforce of power, \nand rescue princess zelda, who holds the triforce of wisdom.")
    print("")
    print(f"{my_hero['name']} has traveled to fire mountain and encountered {villain_1['name']} (Level: {villain_1['level']} Health: {villain_1['health']})")
    print("")
    battle(villain_1)
    print(f"{my_hero['name']} has traveled to the spirit temple and encountered {villain_2['name']} (Level: {villain_2['level']} Health: {villain_2['health']})")
    print("")
    battle(villain_2)
    print(f"{my_hero['name']} has traveled to Gannon's castle and encountered {villain_3['name']} (Level: {villain_3['level']} Health: {villain_3['health']})")
    print("")
    battle(villain_3)
