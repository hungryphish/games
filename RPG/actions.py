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

def shop(player):
  #I want to be sure the shop always has health potions and majika potions available so we find those items fromt he pre-created list
  healthPotion = [p for p in items.potionList if p.name.upper() == 'health potion'.upper()]
  majikElixir = [p for p in items.potionList if p.name.upper() == 'Majik Elixer'.upper()]
  #we use 0 index because the variable is a list and we just want one variable.
  shopInventory = {healthPotion[0]: 5, majikElixir[0]: 5}
  #well get various random items. and then add them to the inventory
  weapons=[items.generateWeapon() for i in range(3)]
  armor=[items.generateArmorPiece() for i in range(3)]
  potions = [random.choice(items.potionList) for i in range(3)]
  randomItems=[weapons+armor+potions]
  #have to go to j because we iterate through a list of lists to get items.
  for i in randomItems:
    for j in i:
      shopInventory[j]=1
  #shop will actually be a character since we can use the existing inventory variable and remove item functions in that class.
  shopKeep=characters.Player('Larry','orc','mage',5000,900,0,shopInventory)

  while True:
    
    def pcPurchase():
      while True:
        print('I have:')
        print([x.name for x in shopKeep.inventory])
        itemName = input('What would you like to buy? ')
        try:
          for i in shopKeep.inventory:
            if i.name.upper() == itemName.upper():
              item=i
              print(f'Oh, my {itemName}?')
              #add in an affirming dialog tree
        except:
          exit=input('Try again again or exit? ')
          if exit.upper() == exit.upper():
            break
          continue
        if player.gold - item.cost < 0:
          print('You dont have the money.')
          exit=input('Try again again or exit? ')
          if exit.upper() == exit.upper():
            break
          continue
        else:
          player.changeGold(-item.cost)
          shopKeep.removeItem(item, 1)
          player.addItem(item, 1)
          print(f'You bought the {item.name}')
          exit=input('Buy again again or exit? ')
          if exit.upper() == exit.upper():
            break
          continue

    def pcSell():
      while True:
        #Got to be a better way of selecting what you want to sell.
        print('You have:')
        print([x.name for x in player.inventory])
        itemName=input('What would you like to sell? ')
        try:
          for i in player.inventory:
            if i.name.upper() == itemName.upper():
              item=i
              print(f'ah your {itemName}')
              #add in an affirming dialog tree
        except:
          exit=input('try again or exit? ')
          if exit.upper() == exit.upper():
            break
          continue
        if shopKeep.gold - item.cost < 0:
          print('I dont have the money')
          continue
        else:
          shopKeep.changeGold(item.cost)
        player.removeItem(item, 1)
        shopKeep.addItem(item, 1)
        print(f'You sold the {item.name}')
        exit=input('Sell again or exit? ')
        if exit.upper() == exit.upper():
          break
        continue

    print('Welcome to the shop!')
    decision=input('Would you like to sell or buy or exit? ')
    if decision.upper() == 'sell'.upper():
      pcSell()
    elif decision.upper() == 'buy'.upper():
      pcPurchase()
    elif decision.upper() == 'exit'.upper():
      break
    else:
      print('Speak up lad!')

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