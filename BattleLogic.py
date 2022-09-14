import random
import sys
from Characters import my_hero
from Characters import villain_1
from Characters import villain_2
from Characters import villain_3

def add_inventory(villain):
    my_hero['equipment'].update(villain['equipment'])
    for inventory_item in villain['equipment']:
        print(f"+ {inventory_item} added to {my_hero['name']}'s inventory.")

def loot_rupies(villain):
    for each in my_hero['rupies']:
        my_hero['rupies'][each] += villain['rupies'][each]
        print(f"+ {villain['rupies'][each]} {each}")
    print(f"{my_hero['name']}'s wallet now contains: \n{my_hero['rupies']}")

def level_up(villain):
    health_increase = random.randrange(30, 50) * my_hero['level']
    my_hero['level'] += 1
    my_hero['health'] += health_increase
    print(f"{my_hero['name']}'s level has increased to {my_hero['level']},\nand {my_hero['name']}'s health has increased by {health_increase}. \nTotal health is now {my_hero['health']}.")
    new_attack_name = input(f"Please name your new attack with your looted weapon: ")
    new_attack_tuple = ((new_attack_name, 35 * my_hero['level']),)
    my_hero['attacks'] += new_attack_tuple
    print(my_hero['attacks'])

def battle(villain):
    while my_hero['health'] > 0:
        my_attack = random.choice(my_hero['attacks'])
        villain['health'] -= my_attack[1]
        if villain['health'] <= 0:
            print(f"{my_hero['name']} has defeated {villain['name']}!")
            print("")
            break
        else:
            print(f"{my_hero['name']} attacked with a {my_attack[0]} causing {my_attack[1]} HP of damage. {villain['name']} has {villain['health']} health left.")
            print("")
        villain_attack = random.choice(villain['attacks'])
        my_hero['health'] -= villain_attack[1]
        if my_hero['health'] <= 0:
            print("You have died")
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
    if my_hero['health'] <= 0:
        sys.exit("You must attempt your adventure again")
    add_inventory(villain_1)
    print("")
    loot_rupies(villain_1)
    print("")
    level_up(villain_1)
    print("")
    print(f"{my_hero['name']} has traveled to the spirit temple and encountered {villain_2['name']} (Level: {villain_2['level']} Health: {villain_2['health']})")
    print("")
    battle(villain_2)
    if my_hero['health'] <= 0:
        sys.exit("You must attempt your adventure again")
    add_inventory(villain_2)
    print("")
    loot_rupies(villain_2)
    print("")
    level_up(villain_2)
    print("")
    print(f"{my_hero['name']} has traveled to Gannon's castle and encountered {villain_3['name']} (Level: {villain_3['level']} Health: {villain_3['health']})")
    print("")
    battle(villain_3)
    if my_hero['health'] <= 0:
        sys.exit("You must attempt your adventure again")
    add_inventory(villain_3)
    print("")
    loot_rupies(villain_3)
    print("")
    level_up(villain_3)
    if my_hero['health'] > 0:
        print("Congratulations, you have defeated Gannon and regained the triforce of power!\nYou, along with Princess Zelda and her triforce of wisdom \nwill keep balance and peace in Hyrule.")
        print("")
    
