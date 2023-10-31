"""tic tac toe game"""

''' Functions '''

def printBoard():
    print("\t   A    B     C     ")
    for n in range(1,10):
        if n%3 == 0 and n != 9:
            print("\t ____|_____|_____")
        elif n == 2:
            print(f"\t1 ",board[0][0],"|","",board[0][1],"","|","",board[0][2]," ")
        elif n== 5:
            print(f"\t2 ",board[1][0],"|","",board[1][1],"","|","",board[1][2]," ")
        elif n == 8:
            print(f"\t3 ",board[2][0],"|","",board[2][1],"","|","",board[2][2]," ")
        else:
            print("\t "," "*2,"|"," "*3,"|"," "*3)

#Function to get move from the player. Translates a human input to indices.
def getMove():
    moveDict = {"a":0,"b":1,"c":2}
    move = input("Which column/row? ").lower()
    move = list(move)
    #Error handling. If user uses a column not in the dict, default move will be checked as invalid.
    try:
        move[0]=moveDict[move[0]]
    except:
        move[0] = 3
    #Subtract 1 because indices begin at 0 but row names begin at 1.
    move[1]=int(move[1])-1
    return(move)

#Check to see if the move is valid.
#Invalid if move is outside the range of the board or cell is already occupied.
def checkMove(move, board):
    valid = True
    #Range check
    if move[0] >= 3 or move[0] <0 or move[1] >= 3 or move[1] <0:
        valid = False
    #Occupied check
    elif board[move[1]][move[0]] != " ":
        valid = False
    return(valid)

#Update the nested list containing all values within the board.
def updateBoard(board, move, player):
    if player == 1:
        symbol = "X"
    else:
        symbol = "O"
    board[move[1]][move[0]] = symbol
    return(board)

#Check to see if there is a win. 8 win conditions.
def checkWins(board):
    for row in range(len(board)):
        #check if all cells in a row are equal
        if board[row][0] == board[row][1] == board[row][2] != " ":
            win = True
            break
        #check if all cells in a column are equal
        elif board[0][row] == board[1][row] == board[2][row] != " ":
            win = True
            break
        #Check diagonal 1
        elif board[0][0] == board[1][1] ==board[2][2] != " ":
            win = True
            break
        #check diagonal 2
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            win = True
            break
        else:
            win = False
    return(win)

'''Default Variables'''

#Create a board
board = list()
#Iterate through the rows. Add the column number and a value of None.
#Player will reference the column name and row number to assign a value.
#This will change the value of the dictionary
for r in range(3):
        board.append([" "," "," "])

win=False

'''Game Loop'''

print("Welcome to tic-tac-toe")
while win == False:
    #Player 1
    #Second loop used so that if a player enters an invalid move, they can redo it.
    valid = False
    while valid == False:
        printBoard()
        print("Player 1 turn")
        p1Move=getMove()
        if checkMove(p1Move, board) == False:
            print("please try again")
            continue
        else:
            valid = True
    board=updateBoard(board,p1Move,1)
    win = checkWins(board)
    if win == True:
        printBoard()
        print("Player 1 wins!!!")
        break

    #Player 2
    valid = False
    while valid == False:
        printBoard()
        print("Player 2 turn")
        p2Move=getMove()
        if checkMove(p2Move, board) == False:
            print("please try again")
            continue
        else:
            valid = True
    board=updateBoard(board,p2Move,2)
    win = checkWins(board)
    if win == True:
        printBoard()
        print("Player 2 wins!!!")
        break
