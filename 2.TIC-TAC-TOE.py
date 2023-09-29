# A program to create a game "TIC-TAC-TOE".

import random
import sys

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
CurrentPlayer = "X"
winner = None
gamerunning = True

# To select the game mode-

game = int(input("Type 1 for Single player, Type 2 for Multiplayer : "))
if game == 1:
    def computer(board):
        while CurrentPlayer == "O":
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                switchplayer()

# To print the game board-

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# To take input from the player-

def playerinput(board):
    inp = int(input("Enter a no. from 1-9: "))

    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = CurrentPlayer
    elif board[inp-1] != "-":
        while board[inp-1] != "-":
            print("Oops player is already in the spot!")
            inp = int(input("Enter a no. from 1-9: "))
            if board[inp-1] == "-":
                board[inp-1] = CurrentPlayer
                break

# To check for win or tie-

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[7] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# To check if it's a tie-

def checktie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gamerunning = False
        sys.exit()

# To check if a player win-

def checkwin():
    if checkdiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        gamerunning = False
        sys.exit()

# To switch the player-

def switchplayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"

# To check for win or tie again-

while gamerunning:
    printBoard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    if game == 1:
        computer(board)
    checkwin()
    checktie(board)