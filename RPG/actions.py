import random
import characters
import utilities
import items
from characters import Character

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

def lobby(player):
  while True:
    print('What would you like to do?')
    choice=input('1. Shop\n 2. Fight\n')
    if choice.upper() == '1' or choice == 'shop'.upper():
      shop(player)
    elif choice.upper() == '2' or choice == 'fight'.upper():
      attackRound(player, characters.generateCharacter('Rando1'))
    else:
      print('Say again?')
      continue
    
def shop(player):
    print('Welcome to the shop.')
    
    while True:
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
      affirmitives=['1', 'YES']

      def pcPurchase():
        while True:
          print('I have:')
          inventoryList=list(shopKeep.inventory.keys())
          # print in a readable manner.
          for index, item in enumerate(inventoryList):
            print(f"{index + 1}. {item.cost}gp  {item.name}")
          #Test to ensure player has a valid selciton.
          try:
            item = input("What would you like to buy?\n")
            item = inventoryList[int(item)-1]
            print(f'A {item.name} for {item.cost}gp?')
            validate=input('1. Yes\n2. No\n')
            if validate.upper() in affirmitives:
              if player.gold - item.cost < 0:
                print('You dont have the money.')
              else:
                player.changeGold(-item.cost)
                shopKeep.removeItem(item, 1)
                player.addItem(item, 1)
                print(f'You bought the {item.name} for {item.cost}gp')
            break
          except:
            print('Doesnt sound right.')
            break

      def pcSell():
        while True:
          #Unequip weapon when going into store.
          try:
            playerWeapon=player.weapon
            player.unequipWeapon()
          except:
            pass
          try:
            playerArmor=player.armor
            player.unequipArmor()
          except:
              pass
          #Test if player has anything to sell. Exit if they dont.
          if len(player.inventory) < 1:
            print('You have nothing to sell.')
            break
          else:
            #Display items
            print('You have:')
            #convert the item names to a list which is ordered and wont change.

            inventoryList=list(player.inventory.keys())
            # print in a readable manner.
            for index, item in enumerate(inventoryList):
              print(f"{index + 1}. {item.cost}gp  {item.name}")
            #Test to ensure player has a valid selciton.
            try:
              print(f'I have {shopKeep.gold}gp.')
              item= input("What would you like to sell?\n")
              item=inventoryList[int(item)-1]
              print(f'Your {item.name} for {item.cost}gp?')
              validate=input('1. Yes\n2. No\n')
              if validate.upper() in affirmitives:
                if shopKeep.gold - item.cost < 0:
                  print('I dont have the money.')
                else:
                  shopKeep.changeGold(item.cost)
                  player.removeItem(item, 1)
                  shopKeep.addItem(item, 1)
                  print(f'You sold the {item.name} for {item.cost}gp.')
                  #If the player didn't sell their weapon, we want to auto-equip it.
                  if item.name != playerWeapon.name:
                    player.setWeapon(playerWeapon)
                  elif item in playerArmor:
                    player.armor=[piece for piece in playerArmor if piece != item]
                  else:
                    for piece in playerArmor:
                      player.equipArmor(piece)

              break
            except:
              print('Doesnt sound right.')
              break
      print(f'You have {player.gold}gp.')
      print('Would you like to: \n1. Buy \n2. Sell \n3. Exit')
      decision=input('')
      if decision == '1' or decision.upper() == 'buy'.upper():
        pcPurchase()
      elif decision == '2' or decision.upper() == 'sell'.upper():
        pcSell()
      elif decision == '3' or decision.upper() == 'exit'.upper():
        break
      else:
        print('Speak up lad!')
        continue


#Battle
#Pick attack.
#Add bonuses to users attack.
#Deplete majika.
#See if attack hits.
#if so, add any bonuses to damage.
#subtract from targets health

# def battle(attacker, )



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