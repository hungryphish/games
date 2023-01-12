import random
import utilities


class Enemy:
  def __init__(self,race,con,str):
    self.race=race
    self.con=con
    self.str=str

  def setArmor(self, armor):
    self.armor=armor
  
  def getHealth(self):
    self.totalAR=utilities.getTotalAR(self.armor)
    for stat in self.totalAR:
      stat += self.con
    self.health=utilities.getTotalAR(self.armor)+self.con
    

goblin=Enemy('goblin',3,2)
goblin.setArmor(utilities.getAllArmor())
for a in goblin.armor:
  print(a.AR)
x=utilities.getTotalAR(goblin.armor)
print(x)
print(goblin.getHealth())