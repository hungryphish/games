import random

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
  'sword':(1,0,7,0,(1,6)), 'mace':(1,0,0,7,(1,6)), 'axe':(1,0,7,0,(1,6)), 'rapier':(1,7,0,0,(1,6)),
  'spear':(2,8,0,0,(2,6)), 'halbred':(2,0,8,0,(2,6)), 'staff':(2,0,0,8,(2,6))
  }
armorSlots=['head','chest','legs','feet']
#material may or may not give a bonus to block a damage type
materials = {'leather':(0,1,0), 'scale':(1,1,0),'plate':(2,2,1)}
#each piece gives a base bonus to block each damage type
armorPieces= {'helmet':('head',1),'cuirass':('chest',2),'greaves':('legs',1),'boots':('feet',1)}

# choices=[piece for piece in armorPieces if armorPieces[piece][0] == 'legs']
# piece = random.choice(choices)
# print(piece)

class Armor:
  itemType='armor'
  def __init__(self, name, slot, AR):
    self.name=name
    self.slot=slot
    self.AR=AR


class Weapon:
  itemType = 'weapon'
  def __init__(self, name, baseAttack, attackType, hands, damageDice):
    self.hands = hands
    self.name = name
    self.baseAttack = baseAttack
    #maybe calculate this in the class as opposed to being fed it.
    self.attackType = attackType
    self.damageDice = damageDice

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
    damageDice = possibleWeapons[weapon][4]
    baseAttack = [possibleWeapons[weapon][1],possibleWeapons[weapon][2],possibleWeapons[weapon][3]]
    for index, attackScore in enumerate(baseAttack):
        if attackScore > 0:
            if index == 0:
                attackType = p
                attackScore+=prefixes[prefix]
            elif index == 1:
                attackType= s
                attackScore+=prefixes[prefix]
            elif index == 2:
                attackType= b
                attackScore+=prefixes[prefix]

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
        
    weapon=Weapon(name, baseAttack,attackType, hands, damageDice)
    return(weapon)


def generateArmorPiece(slot=None):
    #determines if function is generating any piece or a certain type.
    if slot == None:
        slot = random.choice(armorSlots)
    else:
        slot = slot
    choices=[piece for piece in armorPieces if armorPieces[piece][0] == slot]
    piece = random.choice(choices)

    #get AR modifiers
    material = random.choice(list(materials.keys()))
    prefix=random.choice(prefixWeighted)
    suffix=random.choice(suffixesWeighted)
    aspect = random.choice(list(aspects.keys()))

    #calculate base AR before suffix
    AR=[stat + armorPieces[piece][1] for stat in materials[material]]

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

    armor=Armor(name,piece,AR)
    return(armor)

#below function generatres a random piece of armor for each slot.
def getAllArmor():
    armorPieces=[generateArmorPiece(slot) for slot in armorSlots]
    return(armorPieces)

