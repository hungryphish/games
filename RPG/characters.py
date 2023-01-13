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
allSpecies={
  'Human':(True,75,25,50,50,100),
  'Dwarf':(True,75,25,50,100,50),
  'Elf':(True,50,75,100,50,25),
  'Orc':(True,75,50,50,100,25),
  'Ent':(True,100,75,25,50,50),
  'Goblin':(False,50,25,50,100,75),
  'Troll':(False,100,25,50,75,50),
  'Dark Elf':(False,50,100,75,50,25),
  'Lizard Person':(False,75,50,100,25,50),
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

#everyone will be of class Character. Enemies and players will be different subclasses.
#default species is human and default archetype is default
class Character:
 
  def __init__(self, name, species='Human',archetype='Default'):
    self.name=name
    self.species=species
    self.archetype=archetype
    #calling this function gives a character default stats.
    self.getBaseStats()
  
  #Function will provide the base stats of a character based on it's species and archetype. Useful when creating characters.
  def getBaseStats(self):
    self.health=allSpecies[self.species][1]+archetypes[self.archetype][0]
    self.majika=allSpecies[self.species][2]+archetypes[self.archetype][1]
    self.agility=allSpecies[self.species][3]+archetypes[self.archetype][2]
    self.strength=allSpecies[self.species][4]+archetypes[self.archetype][3]
    self.luck=allSpecies[self.species][5]+archetypes[self.archetype][4]

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
  def setWeapon(self, weapon=items.Weapon('Stick',[0,0,1],'blunt',1,1,6)):
    self.weapon=weapon
  
  #add armor
  #Provides a default piece of armor with no AR
  def setArmor(self, armorPieces=[items.Armor('None','None',[0,0,0])]):
    self.armor=armorPieces
    self.AR = utilities.getTotalAR(self.armor)