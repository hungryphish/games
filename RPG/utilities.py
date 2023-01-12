from generators import generateArmorPiece

#below function determies the total armor rating of all armor pieces
def getTotalAR(armorPieces):
  totalAR=[0,0,0]
  for piece in armorPieces:
    for index, stat in enumerate(piece.AR):
      totalAR[index]=totalAR[index]+stat
  return(totalAR)

#below function generatres a random piece of armor for each slot.
def getAllArmor():
    armorSlots=['helmet', 'cuirass', 'greaves', 'boots']
    armorPieces=[generateArmorPiece(slot) for slot in armorSlots]
    return(armorPieces)