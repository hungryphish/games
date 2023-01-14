import random
import os
import actions
import characters
import items
import utilities




buck = characters.Character('Buck','Human', 'Knight')
buck.setWeapon(items.generateWeapon())
print(buck.AR)
buck.setArmor(items.getAllArmor())
# print(buck.AR)
print(buck.weapon.name)

print([x.AR for x in buck.armor])
print(buck.AR)
rando = characters.generateCharacter('Rando')

def battle(attacker, defender):
    while attacker.health > 0 and defender.health > 0:
        actions.attackRound(attacker,defender)
        if attacker.health > 0 and defender.health > 0:
            actions.attackRound(defender,attacker)
    if attacker.health > 0:
        print(f'{attacker.name} is victorious')
    else:
        print(f'{defender.name} is victorious')


battle(buck,rando)