class Armor:
  itemType='armor'
  def __init__(self, name, piece, AR):
    self.name=name
    self.piece=piece
    self.AR=AR

#add secondary damage and type
class Weapon:
  itemType = 'weapon'
  def __init__(self, name, baseAttack, attackType, hands, die, dieSides):
    self.hands = hands
    self.name = name
    self.baseAttack = baseAttack
    #maybe calculate this in the class as opposed to being fed it.
    self.attackType = attackType
    self.die = die
    self.dieSide = dieSides