
import random
import characters
import utilities
'''
To Do:
debug, for some reason, not working correctly. Attacks and block seem to add to one another.
'''

def attack(attacker, defender):
    attack=attacker.weapon.baseAttack
    block=defender.AR
    print(f'{attacker.name} base attack is {attack}')
    print(f'{defender.name} base block is {block}')
    #two coin are flipped to see which if any characters are lucky.
    attackCoin=utilities.dieRoll(1,2)
    defendCoin=utilities.dieRoll(1,2)
    #If attacker is lucky, we add luck to their to hit score.  
    attackRoll = utilities.dieRoll(1,20)
    blockRoll = utilities.dieRoll(1,20)
    print(f'attack roll is {attackRoll}')
    print(f'block roll is {blockRoll}')
    if attackCoin%2 == 0:
        print('Attack luck')
        for index, type in enumerate(attack):
            attack[index] += (attackRoll+attacker.luck)
    else:
        for index, type in enumerate(attack):
            attack[index] += (attackRoll)
    #If oponent is lucky, we add luck to their to block score.
    if defendCoin%2 == 0:
        print('Block luck')
        for index, type in enumerate(block):
            block[index] += (blockRoll+defender.luck)
    else:
        for index, type in enumerate(block):
            block[index] += (blockRoll)
    print(f'Attack total {attack}')
    print(f'Block roll {block}')
    #if attacker does hit, damage is calculated and health is removed from defender.
    hit=False
    for index, type in enumerate(attack):
        if type >= block[index]:
            hit=True
    if hit == True:
        damage=utilities.dieRoll(1,6)+5
        defender.changeStat('health',-damage)
        print(f'Hit for {damage}')
        print(f'{defender.name} has {defender.health} HP remaining')
        print(f'{attacker.name} has {attacker.health} HP remaining')
    else:
        print('Miss!')