import random
import sys, time
from colorama import Fore
from Characters import my_hero
from Characters import villain_1
from Characters import villain_2
from Characters import villain_3

start_text = f"{Fore.YELLOW}{my_hero['name']}, you wield the triforce of courage. \nYou must embark on a quest to defeat Gannon, an evil demon who holds the triforce of power, \nand rescue princess zelda, who holds the triforce of wisdom."
fire_mountain_text = f"{Fore.LIGHTRED_EX}{my_hero['name']} has traveled to fire mountain and encountered {villain_1['name']}, a giant fire breathing serpent. (Level: {villain_1['level']} Health: {villain_1['health']})"
spirit_temple_text = f"{Fore.CYAN}{my_hero['name']} has traveled to the spirit temple and encountered {villain_2['name']}, magical witches wielding the elements. (Level: {villain_2['level']} Health: {villain_2['health']})"
gannons_castle_text = f"{Fore.RED}{my_hero['name']} has traveled to Gannon's castle and encountered {villain_3['name']} (Level: {villain_3['level']} Health: {villain_3['health']})"
epilogue_text = f"{Fore.YELLOW}Congratulations, you have defeated Gannon and regained the triforce of power!\nYou, along with Princess Zelda and her triforce of wisdom \nwill keep balance and peace in Hyrule."

def slow_print(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")

def battle(villain):
    while my_hero['health'] > 0:
        my_attack = random.choice(my_hero['attacks'])
        villain['health'] -= my_attack[1]
        
        my_killing_blow_text = f"{Fore.GREEN}{my_hero['name']} attacked with a {my_attack[0]} ({my_attack[1]} DMG). {villain['name']} has 0 health left."
        my_attack_text = f"{Fore.GREEN}{my_hero['name']} attacked with a {my_attack[0]} ({my_attack[1]} DMG). {villain['name']} has {villain['health']} health left."
        victory_text = f"{Fore.GREEN}{my_hero['name']} has defeated {villain['name']}!"

        if villain['health'] <= 0:
            slow_print(my_killing_blow_text)
            slow_print("")
            slow_print(victory_text)
            slow_print("")
            break
        else:
            slow_print(my_attack_text)
            slow_print("")

        villain_attack = random.choice(villain['attacks'])
        my_hero['health'] -= villain_attack[1]
        
        villain_attack_text = f"{Fore.RED}{villain['name']} attacked with a {villain_attack[0]} ({villain_attack[1]} DMG). {my_hero['name']} has {my_hero['health']} health left."
        villain_killing_blow_text = f"{Fore.RED}{villain['name']} attacked with a {villain_attack[0]} ({villain_attack[1]} DMG). {my_hero['name']} has 0 health left."
        
        if my_hero['health'] <= 0:
            slow_print(villain_killing_blow_text)
            slow_print("")
            death()
        else:
            slow_print(villain_attack_text)
            slow_print("")

def death():
    print(f"{Fore.RED}You have died...")
    sys.exit(f"{Fore.WHITE}You must attempt your adventure again")

def add_inventory(villain):
    my_hero['equipment'].update(villain['equipment'])
    for inventory_item in villain['equipment']:
        slow_print(f"{Fore.WHITE}+ {inventory_item} added to {my_hero['name']}'s inventory.")

def loot_rupies(villain):
    for each in my_hero['rupies']:
        my_hero['rupies'][each] += villain['rupies'][each]
        slow_print(f"+ {villain['rupies'][each]} {each}")
    slow_print("")
    slow_print(f"{Fore.WHITE}{my_hero['name']}'s wallet now contains: \n{my_hero['rupies']}")

def level_up():
    health_increase = random.randrange(40, 50) * my_hero['level']
    my_hero['level'] += 1
    my_hero['health'] += health_increase
    slow_print(f"{Fore.WHITE}{my_hero['name']}'s level has increased to {my_hero['level']},\nand {my_hero['name']}'s health has increased by {health_increase}. \nTotal health is now {my_hero['health']}.")
    print("")
    new_attack_name = input(f"{Fore.YELLOW}Please name your new attack with your looted weapon: ")
    new_attack_tuple = ((new_attack_name, 35 * my_hero['level']),)
    my_hero['attacks'] += new_attack_tuple

def remove_useless_attacks():
    slow_print(f"{Fore.YELLOW}Defeating Gannon will not be easy, you should discard your childhood weapons and use what you have gained on your journey")
    list_of_attacks = list(my_hero['attacks'])
    removed_attack_1 = list_of_attacks.pop(1)
    removed_attack_2 = list_of_attacks.pop(1)
    my_hero['attacks'] = tuple(list_of_attacks)
    slow_print(f"{Fore.WHITE}{removed_attack_1} and {removed_attack_2} have been removed from your attacks.")

def battle_victory(villain):
    add_inventory(villain)
    print("")
    loot_rupies(villain)
    print("")
    level_up()

def run_game():
    slow_print("")
    slow_print(start_text)
    slow_print("")
    slow_print(fire_mountain_text)
    slow_print("")
    battle(villain_1)
    battle_victory(villain_1)
    slow_print("")
    slow_print(spirit_temple_text)
    slow_print("")
    battle(villain_2)
    battle_victory(villain_2)
    slow_print("")
    remove_useless_attacks()
    slow_print("")
    slow_print(gannons_castle_text)
    slow_print("")
    battle(villain_3)
    battle_victory(villain_3)
    slow_print("")
    slow_print(epilogue_text)
    slow_print("")
    
