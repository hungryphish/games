import random
import items
import characters
s='slash'
b='blunt'
p='pierce'
prefixes = {'broken':-2,'peasant':-1,'common':0,'shining':1,'legendary':2}
suffixes={'none':0,'modest': 1, 'cruel': 2, 'vicious':3}
aspects={'giant':b, 'serpent':p, 'tiger':s}
#Weighted lists are there so that the functions are more likely to return some attributes vs others.
prefixWeighted=['broken']*2+['peasant']*13+['common']*68+['shining']*14+['legendary']*3
suffixesWeighted=['none']*62+['modest']*23+['cruel']*10+['vicious']*5
#Weapon values are read as follows: hands, pierce, slash, blunt, num of die, die sides
possibleWeapons={
  'sword':(1,0,7,0,1,6), 'mace':(1,0,0,7,1,6), 'axe':(1,0,7,0,1,6), 'rapier':(1,7,0,0,1,6),
  'spear':(2,8,0,0,2,6), 'halbred':(2,0,8,0,2,6), 'staff':(2,0,0,8,2,6)
  }

#Stats used throughout game.
#Health will be modified by armor
#Majika is used for spell casting
#Agility is used to determine success for ranged attacks and dodge
#Strength is used to determine success for melee attacks and gives new tiers for armor and weapons
#Luck determines dodge success, hit success, and loot
stats=['Health','Majika','Agility','Strength','Luck']
#Different species used throught the game. (Player Race?, Health, Majika, Agility, Strength, Luck)
allSpecies={
  'Human':(True,75,25,50,50,100),
  'Dwarf':(True,75,25,50,100,50),
  'Elf':(True,50,75,100,50,25),
  'Orc':(True,75,50,50,100,25),
  'Ent':(True,100,75,25,50,50),
  'Goblin':(False,50,25,50,100,75),
  'Troll':(False,100,25,50,75,50),
  'Dark Elf':(False,50,100,75,50,25),
  'Lizrd Person':(False,75,50,100,25,50),
  'Mushroom Person':(False,50,75,50,25,100)
  }
#Archetypes used that add to base stats. (Health, Majika, Agility, Strength, Luck)
archetypes={
  'Knight':(60,5,15,60,10),
  'Berserker':(40,10,10,60,30),
  'Ranger':(30,30,50,20,20),
  'Mage':(20,100,15,5,10),
  'Thief':(30,20,30,20,50),
  'Archer':(30,10,70,15,25),
  'Default':(0,0,0,0,0)
}

def generateArmorPiece(type=None):
    s='slash'
    b='blunt'
    p='pierce'
    #each piece gives a base bonus to block each damage type
    armorPieces= {'helmet':1,'cuirass':2,'greaves':1,'boots':1}
    #material may or may not give a bonus to block a damage type
    materials = {'leather':(0,1,0), 'scale':(1,1,0),'plate':(2,2,1)}

    #determines if function is generating any piece or a certain type.
    if type == None:
        piece = random.choice(list(armorPieces.keys()))
    else:
        piece = type
    #get AR modifiers
    material = random.choice(list(materials.keys()))
    prefix=random.choice(prefixWeighted)
    suffix=random.choice(suffixesWeighted)
    aspect = random.choice(list(aspects.keys()))

    #calculate base AR before suffix
    AR=[stat + armorPieces[piece] for stat in materials[material]]

    if suffix == 'none':
        name = ' '.join([prefix,material,piece])
    #modify AR and armor name if there is a suffix
    else:
        name = ' '.join([prefix,material,piece,'of the',suffix,aspect])
    if aspects[aspect] == p:
        AR[0]+suffixes[suffix]
    elif aspects[aspect] == s:
        AR[1]+suffixes[suffix]
    elif aspects[aspect] == b:
        AR[2]+suffixes[suffix]

    armor=items.Armor(name,piece,AR)
    return(armor)

def generateWeapon(type=None):
    #Determines if we are generating a truly random weapon, or just giving a type of weapon random attributes.
    if type == None:
        weapon = random.choice(list(possibleWeapons.keys()))
    else:
        weapon=type
    #retrieves random key values. stored to add as a name later.
    prefix=random.choice(prefixWeighted)
    suffix=random.choice(suffixesWeighted)
    aspect=random.choice(list(aspects.keys()))
    hands = possibleWeapons[weapon][0]
    die = possibleWeapons[weapon][4]
    dieSides = possibleWeapons[weapon][5]

    baseAttack = [possibleWeapons[weapon][2],possibleWeapons[weapon][3],possibleWeapons[weapon][4]]
    for index, dmg in enumerate(baseAttack):
        if dmg > 0:
            if index == 0:
                attackType = p
                dmg+=prefixes[prefix]
            elif index == 1:
                attackType= s
                dmg+=prefixes[prefix]
            elif index == 2:
                attackType= b
                dmg+=prefixes[prefix]

    if suffixes[suffix] !=0:
        if aspects[aspect] == p:
            baseAttack[0] += suffixes[suffix]
        elif aspects[aspect] == s:
            baseAttack[1] += suffixes[suffix]
        elif aspects[aspect] == b:
            baseAttack[2] += suffixes[suffix]
        name=" ".join([prefix,weapon,'of the',suffix,aspect])
    else:
        name=" ".join([prefix,weapon])
        
    weapon=items.Weapon(name, baseAttack,attackType, hands, die, dieSides)
    return(weapon)

# def generateCharacter(species=None,archetype=):
    