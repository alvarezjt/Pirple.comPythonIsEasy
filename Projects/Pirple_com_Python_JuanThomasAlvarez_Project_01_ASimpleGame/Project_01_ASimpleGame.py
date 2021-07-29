"""
Project #1: A Simple Game
Details:
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in Python. Before you get started, 
please watch this video on the rules of Connect 4: https://youtu.be/utXzIFEVPjA
Once you've got the rules down, your assignment should be fairly straightforward. 
*Done: You'll want to draw the board, and allow two players to take turns placing their pieces on the board 
*Done: (but as you learned above, they can only do so by choosing a column, not a row). 
*Done: The first player to get 4 across or diagonal should win!
*Done: Normally the pieces would be red and black, but you can use X and O instead.
Extra Credit:
*Done: Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package like termcolor into your project. We're going to cover importing later in 
the course, but try and see if you can figure it out on your own. Or you might be able to find unicode characters to use instead, depending on what your system supports. 
Here's a hint: print(u'\u2B24')
"""
import os #Enables the use of colors in the terminal for windows.
os.system("cls")

C4Board=[[],[],[],[],[],[],[]]
PlayerName = "X"
PlayAgain = "Yes"
def makeAPlay(ColumnNumber,Player):
    global C4Board
    Column = []
    if C4Board[ColumnNumber]:
        Column = C4Board[ColumnNumber]
    Column.append(Player)
    C4Board[ColumnNumber] = Column

def thereIsAWinner(Connect4Board):
    global C4Board, PlayerName, PlayAgain
    WinnerDirection = [[0,1],[1,1],[1,0],[1,-1]] #[0]Up, [1]Up-Right, [2]Right, [3]Down-Right
    Player = ""
    for i in range(7):
        if (PlayAgain == "No"):
            break
        try:
            for i2 in range(6):
                if (PlayAgain == "No"):
                    break
                Player = Connect4Board[i][i2]
                for Direction in WinnerDirection:
                    if (PlayAgain == "No"):
                        break
                    try:
                        SecondColumn = i + ((Direction[0])*1)
                        SecondRow = i2 + ((Direction[1])*1)
                        ThirdColumn = i + ((Direction[0])*2)
                        ThirdRow = i2 + ((Direction[1])*2)
                        FourthColumn = i + ((Direction[0])*3)
                        FourthRow = i2 + ((Direction[1])*3)
                        #Prevent Index wrap around for lookup of values in next positions to prevent false winners.
                        if (SecondColumn < 0 or ThirdColumn < 0 or FourthColumn < 0 or SecondRow < 0 or ThirdRow < 0 or FourthRow < 0):
                            continue
                        SecondPosition = Connect4Board[SecondColumn][SecondRow]
                        ThirdPosition = Connect4Board[ThirdColumn][ThirdRow]
                        FourthPosition = Connect4Board[FourthColumn][FourthRow]
                    except:
                        #SecondPosition = ""
                        #ThirdPosition = ""
                        #FourthPosition = ""
                        continue
                    if (Player == SecondPosition and Player == ThirdPosition and Player == FourthPosition):
                        print("The winner is " + Player)
                        C4Board=[[],[],[],[],[],[],[]]
                        PlayerName = Player
                        while (True):
                            PlayAgain = input("Play again? Yes/No: ")
                            if (PlayAgain == "Yes"):
                                C4Board=[[],[],[],[],[],[],[]]
                                drawTheBoard(C4Board)
                                break
                            elif (PlayAgain == "No"):
                                break
                            else:
                                continue

        except:
            Player = ""
    if len(Connect4Board[0])>=3:
        return True
    else:
        return False

def drawTheBoard(Connect4Board):
    print("\n")
    for i in range(5,-1,-1):
        for i2 in range(7):
            try:
                if (Connect4Board[i2][i] == "X"):
                    print("| \u001b[31m" + Connect4Board[i2][i] + "\u001b[37m ", end="")
                elif (Connect4Board[i2][i] == "O"):
                    print("| \u001b[32m" + Connect4Board[i2][i] + "\u001b[37m ", end="")
            except:
                print("|   ", end="")
        print("|")
    print("  1   2   3   4   5   6   7")

drawTheBoard(C4Board)

while (True):
    if (PlayAgain == "No"): #Check if user wishes to play again, the default is Yes.
        break

    try:
        PlayedInput = input("\nType reset to start over and exit to close.  \nWhich column do you wish to play? ")
        PlayedColumn = int(PlayedInput)
        if (PlayedColumn < 1 or PlayedColumn > 7):
            print("Please enter a column number 1 through 7, reset or exit.")
            print(u'\u2B24') #test
            continue
    except:
        if (PlayedInput == "exit"):
            break
        if (PlayedInput == "reset"):
            C4Board=[[],[],[],[],[],[],[]]
            drawTheBoard(C4Board)
        print("***Please enter a column number 1 through 7, reset or exit.***")
        continue
    if len(C4Board[(PlayedColumn - 1)]) < 6:
        if PlayerName == "X":
            makeAPlay((PlayedColumn - 1),"X")
            PlayerName = "O"
        else:
            makeAPlay((PlayedColumn - 1),"O")
            PlayerName = "X"
    else:
        print("\n\n\n***ALERT*** Column " + str(PlayedColumn) + " is full, please enter another column number. ***ALERT***")
    drawTheBoard(C4Board)
    if thereIsAWinner(C4Board):
        continue