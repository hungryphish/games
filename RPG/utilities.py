import random

def dieRoll(numOfDie, sidesOfDie):
  result=0
  for die in range(numOfDie):
    result+=random.randint(1,sidesOfDie)
  return(result)