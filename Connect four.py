#[rows] [columns]
#row 0 = Top 0-5
#column 0 = Left 0-6
import sys
global board
global work
board = [["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"]]

def showBoard():
    print("1   2   3   4   5   6   7")
    for row in range(6):
        print
        for column in range(7):  
            sys.stdout.write(board[row][column] + " | ")
            
    print
    print("**********************")
    print

def checkBottom(column):
    empty = False
    Height = 5
    while (empty == False) and (Height>=-1):
        if board[Height][column] == "_":
            empty = True
            return Height
        else:
            Height = Height-1
            
        if Height == -1:
            Height = 20
            return Height
            
  
def InputP1():
    work = False
    Height = 20
    while work == False:
        choice = int(input("Input Column Player 1 - RED "))
        if choice <8:
            Height = checkBottom((choice-1))
            if (Height != 20):
                work = True
            else:
                    print("Invalid Choice")
        else:
            print("Invalid Column")

    board[Height][choice-1] = "R"
    
def InputP2():
    work = False
    Height = 20
    while work == False:
        choice = int(input("Input Column Player 2 - YELLOW "))
        if choice <8:
            Height = checkBottom((choice-1))
            if (Height != 20):
                work = True
            else:
                    print("Invalid Choice")
        else:
            print("Invalid Column")
       
    board[Height][choice-1] = "Y"
    



def checkRows(letter):
    for row in range(6):
        for column in range(5):
            if (board[row][column]== letter) and (board[row][column+1]== letter)and (board[row][column+2]== letter)and (board[row][column+3]== letter):
                if letter== "R":
                    print("P1 winner")
                elif letter == "Y":
                    print("P2 winner")
                sys.exit()

def checkColumns(letter):
     for column in range (7):
         for row in range(3):
             if (board[row][column]== letter) and (board[row+1][column]== letter)and (board[row+2][column]== letter)and (board[row+3][column]== letter):
                if letter== "R":
                    print("P1 winner")
                elif letter == "Y":
                    print("P2 winner")
                sys.exit()

def checkDiagonalsR(letter):
    for row in range(6):
      for column in range(3):
          if (board[row][column]== letter) and (board[row-1][column+1]== letter)and (board[row-2][column+2]== letter)and (board[row-3][column+3]== letter):
            if letter== "R":
                print("P1 winner")
            elif letter == "Y":
                print("P2 winner")
            sys.exit()

def checkDiagonalsL(letter):
    for row in range(5,3,-1):
        for column in range(6,3,-1):
          if (board[row][column]== letter) and (board[row-1][column-1]== letter)and (board[row-2][column-2]== letter)and (board[row-3][column-3]== letter):
            if letter== "R":
                print()
                print("P1 winner")
            elif letter == "Y":
                print()
                print("P2 winner")
            sys.exit()
     
                        
def checkWins(letter):
    checkRows(letter)
    checkColumns(letter)
    checkDiagonalsL(letter)
    checkDiagonalsR(letter)

            
showBoard()
while True:
    InputP1()
    showBoard()
    checkWins("R")
    print
    InputP2()
    showBoard()
    checkWins("Y")
    print

    



    
