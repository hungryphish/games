class Armor:
  itemType='armor'
  def __init__(self, name, piece, AR):
    self.name=name
    self.piece=piece
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