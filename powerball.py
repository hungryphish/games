"""Powerball Simulator"""

import random
#Powerball ticket cost
ticketCost = 2

#Whiteball numbers 1-69 inclusive
whiteNums = range(1,70)

#Redball numbers 1-26 inclusive
redNums = range(1,27)

#Dictionary for win returns. One for if you have the powerball, one for not.
winsNP = {0:0,1:0,2:0,3:7,4:100,5:1000000}
winsP = {0:4,1:4,2:7,3:100,4:50000,5:20000000}

#drawing and ticket are effectively the same. 5 numbers between 1 and 69 and 1 number between 1 and 26
#Below function pulls 5 white balls from the white number list and one red ball.
#Returns a tuple. First is list of white numbers, second is red number.
def draw(whites=5):
    numlst = list()
    numlst = random.sample(whiteNums,whites)
    red=random.choice(redNums)
    return(numlst,red)

#Below function determins how many whites match and if the power balls match.
#Once the number of matches is counted, it references the relevant winning dictionary
#to return the amount you've won in that round.
def getWinnings(ticket,drawing):
    roundWinnings = 0
    matches=0
    #loop through your ticket numbers to see if there is a match. Add to # of matches.
    for n in ticket[0]:
        if n in drawing[0]:
            matches +=1
    #compare the powerball to see if they match.
    if ticket[1] == drawing[1]:
        roundWinnings += winsP[matches]
    else:
        roundWinnings += winsNP[matches]
    return(roundWinnings)

#Below function will let you simulate any number of draws for the powerball.
#Have the ability to simulate multiple tickets for multiple draws. Will always assume you have purchased the same number of tickets for each drawing.
def simulateDraws(numDraws,numTickets=1):
    #counter for number of times we have one
    wins=0
    #counter for how much money we have one
    winnings=0
    #counter for how much money we have spent
    spent=0
    #list to hold drawn tickets
    tickets = list()
    #Loop for draws. Updates results
    for n in range(1,(numDraws+1)):
        drawing = draw()
        for n in range(numTickets):
            spent += ticketCost
            ticket = draw()
            tickets.append(ticket)
        for ticket in tickets:
            roundWinnings = getWinnings(ticket,drawing)
            if roundWinnings > 0:
                wins +=1
                winnings += roundWinnings
    profit = winnings - spent
    winRate = wins/(numDraws+numTickets)
    results = {"wins":wins,"winnings":winnings,"spent":spent,"profit":profit, "win rate":winRate}
    return(results)

#Function to draw until you win the jackpot.
def jackSim():
    #counter for number of times we have one
    wins=0
    #counter for how much money we have one
    winnings=0
    #counter for how much money we have spent
    spent=0
    #num of draws
    numDraws = 0
    jackpot = False
    #Loop. We define what constitutes a jackpot below.
    while jackpot == False:
        spent += ticketCost
        numDraws += 1
        ticket = draw()
        drawing = draw()
        roundWinnings = getWinnings(ticket,drawing)
        if roundWinnings > 0:
            wins +=1
            winnings += roundWinnings
        #Test to see if our predetermined win condition has happened.
        #Can change the second half to any keys in the winsP or winsNp dictionary.
        if roundWinnings == winsNP[4]:
            jackpot = True
    profit = winnings - spent
    winRate = wins/numDraws
    results = {"wins":wins,"winnings":winnings,"spent":spent,"profit":profit, "win rate":winRate, "draws":numDraws}
    return(results)

draws = simulateDraws(1,2)
print(draws)

#simulation = jackSim()
#print(simulation)
