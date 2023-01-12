import random
import items
s='slash'
b='blunt'
p='pierce'
prefixes = {'broken':-2,'peasant':-1,'common':0,'shining':1,'legendary':2}
suffixes={'none':0,'modest': 1, 'cruel': 2, 'vicious':3}
aspects={'serpent':p, 'giant':b, 'wasp':p, 'tiger':s}
#Weighted lists are there so that the functions are more likely to return some attributes vs others.
prefixWeighted=['broken']*2+['peasant']*13+['common']*68+['shining']*14+['legendary']*3
suffixesWeighted=['none']*62+['modest']*23+['cruel']*10+['vicious']*5


def generateArmorPiece(type=None):
    s='slash'
    b='blunt'
    p='pierce'
    #each piece gives a base bonus to block each damage type
    armorPieces= {'helmet':4,'cuirass':6,'greaves':4,'boots':2}
    #material may or may not give a bonus to block a damage type
    materials = {'leather':(0,1,0), 'scale':(1,2,0),'plate':(2,2,1)}

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
    #seperated because one handed and two handed have some common attributes
    oneHanded={'sword':s, 'mace':b, 'axe':s, 'rapier':p}
    twoHanded={'spear':p, 'poleaxe':s, 'staff':b}
    for w in oneHanded:
        oneHanded[w]=(oneHanded[w],4,1)
    for w in twoHanded:
        twoHanded[w]=(twoHanded[w],5,2)
    #merge the two dictionaries into one long one to choose from
    possibleWeapons = oneHanded | twoHanded
    #Determines if we are generating a truly random weapon, or just giving a type of weapon random attributes.
    if type == None:
        weapon = random.choice(list(possibleWeapons.keys()))
    else:
        weapon=type
    #retrieves random key values. stored to add as a name later.
    prefix=random.choice(prefixWeighted)
    suffix=random.choice(suffixesWeighted)
    aspect=random.choice(list(aspects.keys()))
    damageType = possibleWeapons[weapon][0]
    damage = prefixes[prefix]+possibleWeapons[weapon][1]
    reach = possibleWeapons[weapon][2]

    if suffixes[suffix] !=0:
        secondaryDamage = suffixes[suffix]
        secondaryDamageType= aspects[aspect]
        name=" ".join([prefix,weapon,'of the',suffix,aspect])
        weapon=items.Weapon(name,damage,damageType,reach,secondaryDamage,secondaryDamageType)
    else:
        name=" ".join([prefix,weapon])
        weapon=items.Weapon(name,damage,damageType,reach)
    return(weapon)