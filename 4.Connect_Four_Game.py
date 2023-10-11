# Program to create a Connect Four Game.

import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], 
             ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

# To print the Game Board-

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🟡"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🟠"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

# To check for winner-

def checkForWinner(chip):
    def is_inside(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Check horizontal spaces-
    
    for y in range(rows):
        for x in range(cols - 3):
            if all(is_inside(x+i, y) and gameBoard[x+i][y] == chip for i in range(4)):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces-
    
    for x in range(rows):
        for y in range(cols - 3):
            if all(is_inside(x, y+i) and gameBoard[x][y+i] == chip for i in range(4)):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper right to bottom left diagonal spaces-
    
    for x in range(rows - 3):
        for y in range(3, cols):
            if all(is_inside(x+i, y-i) and gameBoard[x+i][y-i] == chip for i in range(4)):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces-
    
    for x in range(rows - 3):
        for y in range(cols - 3):
            if all(is_inside(x+i, y+i) and gameBoard[x+i][y+i] == chip for i in range(4)):
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    return False


def coordinateParser(inputString):
    coordinate = [None] * 2
    if(inputString[0] == "A"):
        coordinate[1] = 0
    elif(inputString[0] == "B"):
        coordinate[1] = 1
    elif(inputString[0] == "C"):
        coordinate[1] = 2
    elif(inputString[0] == "D"):
        coordinate[1] = 3
    elif(inputString[0] == "E"):
        coordinate[1] = 4
    elif(inputString[0] == "F"):
        coordinate[1] = 5
    elif(inputString[0] == "G"):
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

# To check space is empty(available)-

def isSpaceAvailable(intendedCoordinate):
    if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🟠'):
        return False
    elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🟡'):
        return False
    else:
        return True

def gravityChecker(intendedCoordinate):
    
    # Calculate space below
    
    spaceBelow = [None] * 2
    spaceBelow[0] = intendedCoordinate[0] + 1
    spaceBelow[1] = intendedCoordinate[1]
    
    # Is the coordinate at ground level
    
    if(spaceBelow[0] == 6):
        return True
    
    # Check if there's a token below
    
    if(isSpaceAvailable(spaceBelow) == False):
        return True
    return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
    if(turnCounter % 2 == 0):
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space: ")
            coordinate = coordinateParser(spacePicked)
            try:
                
                # Check if the space is available
                
                if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, '🟡')
                    break
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occured. Please try again.")
        winner = checkForWinner('🟡')
        turnCounter += 1
        
    # It's the computers turn
    
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), random.randint(0,5)]
            cpuCoordinate = coordinateParser(cpuChoice)
            if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
                modifyArray(cpuCoordinate, '🟠')
                break
        turnCounter += 1
        winner = checkForWinner('🟠')

    if(winner):
        printGameBoard()
        break
