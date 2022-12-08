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

  #function evaluates a hand and returns its value
  def handValues(hand, handTotal, dealer=False):
    if dealer == False:
      aces=0
      for card in hand:
        #write code to make aces wild here.
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
  
  print(f'You have ${playerMoney}')
  bet = int(input('what do you bet? $'))
  if bet > playerMoney:
    print('you cant do that')
    return(blackJack(playerMoney))
  else:
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
    if dealerTotal == 21:
      if playerTotal != 21:
        result='you lose'
        end=True
      else:
        result='push'
        end=True
    elif playerTotal == 21:
        result='black jack!'
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
        print(f'dealer hand is {dealerHand} for {dealerTotal}')
        while dealerTotal < 17:
          hit(dealerHand)
          dealerTotal=0
          dealerTotal=handValues(dealerHand, dealerTotal)
          print(f'dealer hand is {dealerHand} for {dealerTotal}')
        print(f'dealer has {dealerTotal} you have {playerTotal}')
        if playerTotal > dealerTotal or dealerTotal > 21:
          result='you win'
        elif playerTotal == dealerTotal:
          result='push'
        else:
          result='you lose'
        end=True

  if result == 'black jack!':
    playerMoney=playerMoney+bet*2.5
  elif result == 'you win':
    playerMoney=playerMoney+bet*2
  elif result == "push":
    playerMoney=playerMoney+bet
  print(result)

  if input(f'You have ${playerMoney} would you like to play again? ') == 'y':
    blackJack(playerMoney)
  else:
    print(f'You finished with ${playerMoney}')  
    return()
blackJack(100)