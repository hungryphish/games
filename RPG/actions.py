import random
import characters
import utilities
import items

def characterCreation():
  
  print('Welcome weary slave. Unfortunately, you have reached the end of the line and you are destined to die in these fighting pits. Ive watched hundreds just like you come and go, but my eyes arent what they used to be. What race are you?')
  while True: 
    while True:
      print('*Species available: Human, dwarf, orc, ent, bird person*')
      species = input('*Choose your race: ')
      x=[specie.upper() for specie in characters.speciesNames]
      if x.count(species.upper()) > 0:
        print(f'Ah, I see it now youre a {species.capitalize()}!')
        print('Did I hear you right?')
        if input('Yes or no? ').upper() in ['YES', 'Y']:
          break
        else:
          continue
      else:
        print('No no that cant be it.')


    print('Tell me, before you were a slave, what did you do for a living?')
    while True:
      print('*Archetypes available: Mage, ranger, knight, barbarian, thief, archer*')
      archetype = input('*Choose your archetype: ')
      x=[archetype.upper() for archetype in characters.archetypeNames]
      if x.count(archetype.upper()) > 0:
        print(f'Ah, I see it now youre a {archetype.capitalize()}!')
        print('Did I hear you right?')
        if input('Yes or no? ').upper() in ['YES', 'Y']:
          break
        else:
          continue
      else:
        print('No no that cant be it.')
    print('Wow! I hear that is a dangerous profession.')


    print('My my, hear I am being nosy without even getting your name.')
    while True:
      name = input('What should I write on your tombstone? ')
      if input(f'Is this how you spell it? {name} ').upper() in ['YES', 'Y']:
        break
      else:
        print('Speak up lad! Im an old man.')

    print(f'okay {name} so you are a {species.capitalize()} {archetype.capitalize()}. Is that right?')
    affirmation = input('yes or no? ')
    possibleAs=['YES', 'Y']
    if possibleAs.count(affirmation.upper()) < 1:
      continue
    else:
      playerCharacter = characters.Player(name, species.lower(), archetype.lower())
      return(playerCharacter)

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