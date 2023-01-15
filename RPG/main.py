import random
import os
import actions
import characters
import items
import utilities
import itertools

'''
To Do:
Implement loot
Implement XP gain
Implement Levels
Add more potions
Add store
Character creation can be expanded on to include stats.
add inventory mgmt
add different attacks
should I create a super class for weapons, armor and potions?
'''
#Below will take the user to the character creation screen.
# playerCharacter=actions.characterCreation()
# print(playerCharacter.name)
# print(playerCharacter.species.name)
# print(playerCharacter.archetype.name)


buck = characters.Character('Buck','bird person', 'mage')
print(buck.health)
buck.changeStat(items.healthPotion.stat,items.healthPotion.amount)
print(buck.health)
# buck.setWeapon(items.generateWeapon())
# print(buck.weapon.name)
# # buck.setArmor(items.getAllArmor())
# # print(buck.weapon.name)
# # sparrow = characters.Character('Sparrow','bird person','mage')
# # sparrow.setArmor(items.getAllArmor())
# # sparrow.setWeapon(items.generateWeapon())
# # print(sparrow.weapon.name)
# rando = characters.generateCharacter('Rando')

# def battle(attacker, defender):
#     #get base health so that it can be reset after the fight.
#     ah=attacker.health
#     dh=defender.health
#     while attacker.health > 0 and defender.health > 0:
#         actions.attackRound(attacker,defender)
#         if attacker.health > 0 and defender.health > 0:
#             actions.attackRound(defender,attacker)
#     if attacker.health > 0:
#         victor=attacker
#         print(f'{attacker.name} is victorious')
#     else:
#         print(f'{defender.name} is victorious')
#         victor=defender
#     #resets health so that multiple battles may be fought in a row.
#     attacker.changeStat('health',ah-attacker.health)
#     defender.changeStat('health',dh-defender.health)

#     return(victor.name)

# #below is just for testing
# ls=[]
# for n in range(50):
#     ls.append(battle(buck,sparrow))
# print(ls)

