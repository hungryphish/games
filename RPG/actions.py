import random
import characters
import utilities

#def characterCreation():

#def shop():

def attackRound(attacker, defender):
  '''#We first determine if the atttacker is lucky, if so, they get a bonus to their attack roll.
  total attack is then determined.
  Defender is similar.
  Each attack stat is compared to its coutnerpart block stat. If one of the attack stats is great, attacker scores a hit.
  if defender hits, the weapons hit die is rolled to determine base damage, then strength is added to determine total damage
  damage is removed from defenders health
  Else, defender dodged and this round is over'''
  #Attacker
  if utilities.dieRoll(1,200)+attacker.luck > 150:
    attackRoll = utilities.dieRoll(1,20)+2
    print('Attacker is lucky')
  else:
    attackRoll = utilities.dieRoll(1,20)
  totalAttack = [stat + attackRoll for stat in attacker.attack]
  print(f'Total attack is {totalAttack}')
  
  #Defender
  if utilities.dieRoll(1,200)+defender.luck > 150:
    blockRoll = utilities.dieRoll(1,20)+2
    print('Defender is lucky')
  else:
    blockRoll = utilities.dieRoll(1,20)
  totalBlock = [stat + blockRoll for stat in defender.block]
  print(f'Total block is {totalBlock}')
  
  #compare rolls
  hit = False
  for index, stat in enumerate(totalAttack):
    if stat >= totalBlock[index]:
      hit = True
      
  #Apply damage
  if hit == True:
    damage = attacker.strength
    damage += utilities.dieRoll(attacker.damageDice[0],attacker.damageDice[1])
    defender.changeStat('health',-damage)
    print(f'Hit for {damage}')
    print(f'{defender.name} has {defender.health} HP remaining')
    print(f'{attacker.name} has {attacker.health} HP remaining')
  else:
    print('miss')

#def modifyCharacter():

#def die():