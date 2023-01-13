import random
import actions
import characters
import generators
import items
import utilities

buck=characters.Character('buck','Human','Knight')
goblin = characters.Character('goblin','Goblin')
sparrow = characters.Character('Sparrow','Lizard Person','Mage')

b=generators.generateWeapon()
buck.setWeapon(b)
print(f'bucks weapon attacks for {b.baseAttack}')
sparrow.setWeapon(items.Weapon('Sharp Stick',[10,0,0],'pierce',2,2,6))
print(f'buck has a {b.name}')
print(f'sparrow has a sharp stick')
goblin.setWeapon()
buck.setArmor(utilities.getAllArmor())
for piece in buck.armor:
    print(piece.name)
print(f'Bucks armor is {buck.AR}')
sparrow.setArmor(utilities.getAllArmor())
for piece in sparrow.armor:
    print(piece.name)
print(f'Sparrows armor is {sparrow.AR}')
goblin.setArmor()

# actions.attack(buck, goblin)

while sparrow.health > 0 and buck.health >0:
  print('Sparrow attacks')
  actions.attack(sparrow, buck)
  print('Buck attacks')
  actions.attack(buck, sparrow)

if sparrow.health==0:
    print('sparrow died')
else:
    print('buck died')