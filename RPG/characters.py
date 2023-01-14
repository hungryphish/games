import random
import utilities
import items


#Stats used throughout game.
#Health will be modified by armor
#Majika is used for spell casting
#Agility is used to determine success for ranged attacks and dodge
#Strength is used to determine success for melee attacks and gives new tiers for armor and weapons
#Luck determines dodge success, hit success, and loot
stats=['Health','Majika','Agility','Strength','Luck']
#Different species used throught the game. (Player Race?, Health, Majika, Agility, Strength, Luck)

class Species:
  
  def __init__(self, name, PC, health, majika, agility, strength, luck):
    self.name = name
    self.PC = PC
    self.health = health
    self.majika = majika
    self.agility = agility
    self.strength = strength
    self.luck = luck


    
class Archetypes:
  
  def __init__(self, name, health, majika, agility, strength, luck):
    self.name = name
    self.health = health
    self.majika = majika
    self.agility = agility
    self.strength = strength
    self.luck = luck




#everyone will be of class Character. Enemies and players will be different subclasses.
#default species is human and default archetype is default
class Character:
 
  def __init__(self, name, species, archetype):
    self.name=name
    #calling this function gives a character default stats.
    self.archetype=archetype
    for s in speciesList:
      if s.name.upper() == species.upper():
        self.species=s
    for a in archetypesList:
      if a.name.upper() == archetype.upper():
        self.archetype=a
    self.getBaseStats()
    self.setWeapon()
    self.AR=[0,0,0]
    self.block = [stat + self.agility for stat in self.AR]


  
  #Function will provide the base stats of a character based on it's species and archetype. Useful when creating 
  def getBaseStats(self):
    self.health=self.species.health + self.archetype.health
    self.majika=self.species.majika + self.archetype.majika
    self.agility=self.species.agility + self.archetype.agility
    self.strength=self.species.strength + self.archetype.strength
    self.luck=self.species.luck + self.archetype.luck

  #Change each stat individually. For example, when taking dmg, health stat is changed.
  def changeStat(self, stat, amount):
    if stat == 'health':
      self.health+=amount
    elif stat == 'majika':
      self.majika+=amount
    elif stat == 'agility':
      self.agility+=amount
    elif stat == 'strength':
      self.strength+=amount
    elif stat == 'luck':
      self.luck+=amount
  
  #allows one to change a species.
  def setSpeciess(self, species):
    self.species=species
    self.getBaseStats()
  
  #allows one to change the archetype
  def setClass(self, archetype):
    self.archetype=archetype
    self.getBaseStats()
  
  #add a weapon
  #Provides a default weapon
  def setWeapon(self, weapon=items.Weapon('Stick',[0,0,1],'blunt',1,(1,6))):
    self.weapon = weapon
    #add agility modifier to attack
    self.attack = [stat + self.agility for stat in self.weapon.baseAttack]
    self.damageDice = self.weapon.damageDice
  


  #below function determies the total armor rating of all armor pieces
  def getTotalAR(armor):
    totalAR=[0,0,0]
    for piece in armor:
      for index, stat in enumerate(piece.AR):
        totalAR[index]+=totalAR[index]+stat
    return(totalAR)
  
  #add armor
  #Provides a default piece of armor with no AR
  def setArmor(self, armorPieces):
    self.armor=armorPieces
    self.AR = Character.getTotalAR(self.armor)
    self.block = [stat + self.agility for stat in self.AR]
    
    
class Player(Character):
  #inventory is a dictionary, because each item will have a quantity given.
  def __init__(self, gold=100, level=1, xp=0, inventory={}):
    self.gold = gold
    self.level = level
    self.xp = xp
    self.inventory = inventory
    
  def changeGold(self, gold):
    self.gold+=gold
  
  def changeXP(self, xp):
    self.xp+=xp
  
  def changeLevel(self, level):
    self.level+=level
    
  def addItem(self, item, qty):
    if item in self.inventory:
      self.inventory[item] += qty
    else:
      self.inventory[item] = qty
    
  def removeItem(self, item, qty):
    self.inventory[item] -= qty
    if self.inventory[item] <= 0:
      del self.inventory[item]

  def equipWeapon(self, weapon):
    self.addItem(self.weapon,1)
    self.setWeapon(weapon)
    self.removeItem(weapon, 1)
    
#add armor. Probably means implementing slots.


#initialize species
human = Species('Human',True,75,25,50,50,100)
dwarf = Species('Dwarf',True,75,25,50,100,50)
elf = Species('Elf',True,50,75,100,50,25)
orc = Species('Orc',True,75,50,50,100,25)
ent = Species('Ent',True,100,75,25,50,50)
goblin = Species('Goblin',False,50,25,50,100,75)
troll = Species('Troll',False,100,25,50,75,50)
darkElf = Species('Dark Elf',False,50,100,75,50,25)
lizardPerson = Species('Lizard Person',False,75,50,100,25,50)
mushroomPerson = Species('Mushroom Person',False,50,75,50,25,100)
speciesList=[human,dwarf,elf,orc,ent,goblin,troll,darkElf,lizardPerson,mushroomPerson]
speciesNames=['human', 'dwarf','elf','orc','ent','goblin','troll','dark Elf','lizard Person','mushroom Person']


#Archetypes used that add to base stats. (Health, Majika, Agility, Strength, Luck)
#initialize archetypes
knight = Archetypes('Knight',60,5,15,60,10)
berserker = Archetypes('Berserker',40,10,10,60,30)
ranger = Archetypes('Ranger',30,30,50,20,20)
mage = Archetypes('Mage',20,100,15,5,10)
thief = Archetypes('Thief',30,20,30,20,50)
archer = Archetypes('Archer',30,10,70,15,25)
default = Archetypes('Default',0,0,0,0,0)
archetypesList=[knight,berserker,ranger,mage,thief,archer,default]
archetypeNames=['Knight','Berserker','Ranger','Mage','Thief','Archer','Default']

def generateSpecies():
    species = random.choice(speciesList)
    return(species)

def generateArchetype():
    archetype = random.choice(archetypesList)
    return(archetype)
  
def generateCharacter(name, species=random.choice(speciesNames), archetype=random.choice(archetypeNames)):
  print(species)
  print(archetype)
  character = Character(name,species,archetype)
  return(character)