'''
blackjack
5 deck shoe. When there are less than 2 decks, shoe is pulled and replaced. Dealer draws while hand is below hard 17.
'''

import random
import itertools
def blackJack(money):
  #creating a list of tuples containing all 52 cards in a deck.
  suits=['Diamonds','Hearts','Clubs','Spades']
  cards=[str(i) for i in range(2,11)] + ['J','Q','K','A']
  values=[i for i in range(2,11)]+[10,10,10,11]
  cardValues=dict(zip(cards,values))
  #itertools is same as a nested for loop
  deck = list(itertools.product(cards, suits))
  #Fill the shoe with more decks. Default will be 5.
  deckQty=5
  deck=deck*deckQty
  #shuffle the shoe. all cards will be drawn from this shuffled shoe.
  random.shuffle(deck)

  #function evaluates a hand and returns its value.
  #Dealer is a bool variable so that after the draw, the player only sees one card the dealer has.
  def handValues(hand, handTotal, dealer=False):
    #totals up all cards in hand by referencing the type of card and its value in the cardValues dictionary.
    for card in hand:
      handTotal += cardValues.get(card[0])
    #Since aces can be 11 or 1 and we only want them to be 1 if we are over 21
    #this evaluates if there are any aces and if we are bust.
    #if so, subtract 10 so that the value of the ace is effectively 1.
    for card in hand:
      if card[0] == 'A' and handTotal > 21:
        handTotal -=10
    #This is so after the draw only one of the dealers cards is shown.
    if dealer == True:
      handTotal=cardValues.get(hand[0][0])
    return(handTotal)

  #Function that pulls another card from the deck and adds it to the player or dealers hand.
  def hit(hand):
    hand.append(deck.pop())
    return(hand)

  def gameLoop(deck, money):
    #Initializing variables that will be used throughout the game.
    dealerHand=[]
    dealerTotal=0
    playerHand=[]
    playerTotal=0
    playerMoney=money
    #Bool statement controls the core gameplay loop. Since the game was started by the player, its default is False.
    end=False

    print(f'You have ${playerMoney}')
    bet = int(input('what do you bet? $'))
    #tests if player made a valid bet. Valid bets must be greater than 0 and less than what the player has.
    if bet > playerMoney or bet < 0:
      print('You cant do that')
      return(gameLoop(deck, playerMoney))
    #Subtracts bet from player's money
    else:
      playerMoney-=bet

    #initial deal. Modulo statement is there so that dealer and player alternately receive cards.
    for i in range(4):
      if i % 2 != 0:
        playerHand.append(deck.pop())
      else:
        dealerHand.append(deck.pop())

    #reassign player and dealer hand totals.
    playerTotal=handValues(playerHand,playerTotal)
    dealerTotal=handValues(dealerHand,dealerTotal)

    while end == False:
      #print statements display the players hand and one card of the dealer.
      print(f'Player has {playerHand} for {playerTotal}')
      print(f'Dealer has {dealerHand[0]} for {handValues(dealerHand,dealerTotal,True)}')

      #below are automatic win/loss conditions.
      if dealerTotal == 21:
        if playerTotal != 21:
          result='You lose'
        else:
          result='Push'
        end=True
      elif playerTotal == 21 and len(playerHand) < 3:
          result='Black jack!'
          end=True
      elif playerTotal > 21:
        if dealerTotal <= 21:
          result='Bust'
        else:
          result='Push'
        end=True

      #Player has not auto won/loss. Must decide to hit or stay.
      else:
        decision = input('Would you like to hit? ')
        #decision to hit adds a new card to players hand and kicks back to beginning of while loop, to test if player busted.
        if decision == 'y':
          playerHand = hit(playerHand)
          #Reset the player total so that it isn't counted twice when it is updated on the next line.
          playerTotal=0
          playerTotal= handValues(playerHand, playerTotal)

        #decision ends players moves, displays dealers hand and will evaluate if dealer hits or not.
        if decision == 'n':
          print(f'Dealer hand has {dealerHand} for {dealerTotal}')
          while dealerTotal < 17:
            #similar to player hit.
            hit(dealerHand)
            dealerTotal=0
            dealerTotal=handValues(dealerHand, dealerTotal)
            print(f'Dealer draws {dealerHand[-1]} for {dealerTotal}')

          #following are win loss conditions.
          if playerTotal > dealerTotal or dealerTotal > 21:
            result='You win!'
          elif playerTotal == dealerTotal:
            result='Push'
          else:
            result='You lose'
          end=True
    #below changes the players money based on the result.
    if result == 'Black jack!':
      playerMoney+=(bet*2.5)
    elif result == 'You win!':
      playerMoney+=(bet*2)
    elif result == "Push":
      playerMoney+=bet

    #final output of hand.
    print(f'Player hand is {playerHand} for {playerTotal}')
    print(f'Dealer hand is {dealerHand} for {dealerTotal}')
    print(result)

    #ask the player if they want to play again.
    if input(f'You have ${playerMoney} would you like to play again? ') == 'y':
      #If they do but the deck is smaller than 2 decks. Reset the shoe.
      if len(deck)<104:
        print("Building and shuffling shoe.")
        blackJack(playerMoney)
      #otherwise keep the shoe the way it is and play another hand.
      else:
        gameLoop(deck, playerMoney)
    #ends game
    else:
      print(f'You finished with ${playerMoney}')
      return()
  gameLoop(deck, money)

blackJack(100)
