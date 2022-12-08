'''
blackjack

User and dealer are dealt 2 cards.
User can see noth of their cards, but only one of the dealers.
While the sum of the users cards are below 21 they can perform the following actions:
  hit, a new card is added.
  stay, no cards are added.
  If a user has dealt two of the same card they may split their cards.
    At this point the user has two hands.
    A card is dealt to each hand.
    While the sum of the users cards are below 21...
If the users cards equate to 21
  They stay.
If the users cards are greater than 21
  They bust and lose.

If the user stays or is dealt 21,
  Dealer reveals second card.
  if the sum of the dealers cards is > 21.
    they bust and the player wins.
  If the sum of the dealers cards is >= 17, 
    they stay.
    if they stay and cards are greater than the players,
      house wins.
    if they stay and cards are lower than players,
      player wins.
    else
      push, no one wins.
  If the sum of the dealers cards is less than 16,
    they hit.
'''

import random

def blackJack(money):

  face=['J','Q','K','A']
  suits=['Diamond','Heart','Club','Spade']
  nums=[str(i) for i in range(2,11)]
  cards=nums+face
  values=[i for i in range(2,11)]+[10,10,10,11]
  cardValues=dict(zip(cards,values))
  #create deck
  deck=[]
  for card in cards:
    for suit in suits:
      deck.append((card,suit))
  random.shuffle(deck)

  #function evaluates both hands, returns their value
  def handValues(hand, handTotal, dealer=False):
    if dealer == False:
      for card in hand:
        handTotal=cardValues.get(card[0])+handTotal
    else:
      handTotal=cardValues.get(hand[0][0])
    return(handTotal)
    
  def hit(hand):
    hand.append(deck.pop())
    return(hand)
  

  dealerHand=[]
  dealerTotal=0
  playerHand=[]
  playerTotal=0
  playerMoney=money
  end=False
  
  print(f'You have ${money})
  bet = input('what do you bet? ')
  playerMoney=money-bet
  
  #initial deal.
  for i in range(4):
    if i % 2 != 0:
      playerHand.append(deck.pop())
    else:
      dealerHand.append(deck.pop())
  
  playerTotal=handValues(playerHand,playerTotal)
  dealerTotal=handValues(dealerHand,dealerTotal)

  while end == False:
    print(f'player has {playerHand} for {playerTotal}')
    print(f'dealer has {dealerHand[0]} for {handValues(dealerHand,dealerTotal,True)}')
    if playerTotal == 21:
      if dealerTotal != 21:
        result='black jack!'
        end=True
      else:
        result='push'
        end=True
    elif playerTotal > 21:
      if dealerTotal <= 21:
        result='bust'
        end=True
      else:
        result='push'
        end=True
    else:
      decision = input('Would you like to hit? ')
      if decision == 'y':
        playerHand = hit(playerHand)
        #Reset the player total so that it isn't counted twice when it is updated on the next line.
        playerTotal=0
        playerTotal= handValues(playerHand, playerTotal)
      if decision == 'n':
        print(f'dealer has {dealerTotal}')
        if playerTotal > dealerTotal:
          result='you win'
        elif playerTotal == dealerTotal:
          result='push'
        else:
          result='you lose'
        end=True
  print(result)
  
blackJack(100)
