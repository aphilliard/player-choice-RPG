import os
import math
import random
import sys
import time

global monters
monsters = []
global heroes
heroes = []

def roll(modifier):
    return random.randrange(1,20) + modifier

# make a class for generic creatures including both monsters and heroes
class creature():
    def __init__(self, name, ct):
        self.name = name
        self.creatureType = ct     

    def get_name(self):
        return self.name

    def __repr__(self):
        return '\n{} Name:{} '.format(self.creatureType, self.name)

# make a list of the creatures' traits
creatures = [
            creature('Zombie', 'monster'),
            creature('Skeleton', 'monster'),
            creature('Necromancer', 'monster'),
            creature('Paladin', 'hero'),
            creature('Cleric', 'hero'),
            creature('Knight', 'hero')
            ]

# divide creatures into monsters...
for i in range(len(creatures)):
    if creatures[i].creatureType == 'monster':
        monsters.append(creatures[i])
# ...and heroes        
    elif creatures[i].creatureType == 'hero':
        heroes.append(creatures[i])

whoseTurn = random.choice([True, False])

os.system('clear')
print('3 versus 3 combat demo\n\n')
print('Your 3 heroes must battle 3 monsters.\n\033[91m')
if whoseTurn == True:
    print('Player goes first\033[00m')
else:
    print('Computer goes first\033[00m')

# start the main loop

while True:
    while whoseTurn == True:

        # get player's choices
        print('\n\033[94mYour turn.\n')
        print('These are your targets: \n')
        for i in range(len(monsters)):
            print(i, monsters[i].name)

        # who will player target
        player_target_choice = int(input('Choose target: \n'))
        target_monster = monsters[player_target_choice]
        print(f'You chose to attack {monsters[player_target_choice].name}\n')
            
        # which hero will do the attacking?
        print('These are your heroes: \n')
        for i in range(len(heroes)):
            print(i, heroes[i].name)
        print(f'Who will attack {monsters[player_target_choice].name}?\n')
        player_character_choice = int(input('Choose attacker: \n'))
        print(f'{heroes[player_character_choice].name} will attack {monsters[player_target_choice].name}.\n')

        # hero kills monster
        print(f'{heroes[player_character_choice].name} kills {monsters[player_target_choice].name}!\n')    
            
        # remove the dead monster from the monster list
        monsters.remove(monsters[player_target_choice])
        # check to see if monsters list is empty
        if not monsters:
            print('Player has defeated all monsters!\033[00m')
            raise SystemExit

        # give the player an update on remaining monsters
        print('These monsters remain:')
        for i in range(len(monsters)):
            print(i, monsters[i].name)

            whoseTurn = False

    # Computer's turn
    while whoseTurn == False:
        time.sleep(1)
        print('-------------------------------------')
        print('\n\033[91m\nComputer turn')
        print('Computer has these monsters:\n')
        for i in range(len(monsters)):
            print(i, monsters[i].name)
        print()
        time.sleep(1)
        monster_actor = random.randrange(len(monsters))
        print(f'Computer chooses {monsters[monster_actor].name} to act.\n')
        time.sleep(1)
        monster_target = random.randrange(len(heroes))
        print('Computer can choose to target one of these heroes:')
        for i in range(len(heroes)):
            print(i, heroes[i].name)
        print(f'Computer will target {heroes[monster_target].name}.\n')
        time.sleep(1)
        print(f'{monsters[monster_actor].name} kills {heroes[monster_target].name}!')
        time.sleep(2)        
        # remove the dead hero from the heroes list
        heroes.remove(heroes[monster_target])
        print('These heroes remain:')
        for i in range(len(heroes)):
            print(i, heroes[i].name)
                
        # check to see if all heroes are dead
        if not heroes:
            print('Computer has defeated all heroes!\033[00m')
            raise SystemExit
        whoseTurn = True    