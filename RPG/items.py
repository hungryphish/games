class Armor:
  itemType='armor'
  def __init__(self, name, piece, AR):
    self.name=name
    self.piece=piece
    self.AR=AR

class Weapon:
  itemType = 'weapon'
  def __init__(self, name, damage, damageType, reach, modDamage=0, modDamageType='none'):
    self.reach = reach
    self.name = name
    #if statement is here to not display modifier damage if there is no suffix or aspect
    if modDamage!=0:
      self.damage = (damage, damageType),(modDamage,modDamageType)
    else:
      self.damage = (damage, damageType)