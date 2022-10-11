# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:13:17 2022

@author: Hp
"""

import random
import sys

#Initializing Board
NUM_ROWS = 6
NUM_COLS = 7
board = []
player = []
# Checker for player 1 is X,player 2 is O, player 3 is V, player 4 H and player 5 M
checkers=['X','O','V','H','M']


for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
         row_list.append(' ')
    board.append(row_list)
for i in range(0,NUM_COLS):
        print('  ' + chr(i+65), end=' ')
print("\n +" + "---+" * NUM_COLS)
for row in range(NUM_ROWS):
        print(' |', end=' ')
        for col in range(NUM_COLS):
            print(board[row][col] + ' | ', end='')
        print("\n +"+"---+"*NUM_COLS)


# Function for printing board
def print_board():
    for i in range(0,NUM_COLS):
        print('  ' + chr(i+65), end=' ')
    print("\n +" + "---+" * NUM_COLS)
    for row in range(NUM_ROWS):
            print( ' |', end=' ')
            for col in range(NUM_COLS):
                print(board[row][col] + ' | ', end='')
            print("\n +"+"---+"*NUM_COLS)

# Function to check if there is a win
def check_win(board, checker):
	# Check horizontal win
	for c in range(NUM_COLS-3):
		for r in range(NUM_ROWS):
			if board[r][c] == checker and board[r][c+1] == checker and board[r][c+2] == checker and board[r][c+3] == checker:
				return True

	# Check vertical win
	for c in range(NUM_COLS):
		for r in range(NUM_ROWS-3):
			if board[r][c] == checker and board[r+1][c] == checker and board[r+2][c] == checker and board[r+3][c] == checker:
				return True

	# Check forward diaganols
	for c in range(NUM_COLS-3):
		for r in range(NUM_ROWS-3):
			if board[r][c] == checker and board[r+1][c+1] == checker and board[r+2][c+2] == checker and board[r+3][c+3] == checker:
				return True

	# Check backward diaganols
	for c in range(NUM_COLS-3):
		for r in range(3, NUM_ROWS):
			if board[r][c] == checker and board[r-1][c+1] == checker and board[r-2][c+2] == checker and board[r-3][c+3] == checker:
				return True
# Function for draw
def check_draw(board):
    count = 0
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            
            if board[r][c] != " " :
                count += 1
                
            if count == NUM_ROWS*NUM_COLS:
                print("Game ends in draw\n")
                return True
    return False
# Taking no. of players from user at runtime
num_player=input('Enter No. of players:')
if (int(num_player)<2) | (int(num_player)>5):
    print('The game only supports players between 2 and 5')
    sys.exit()
for x in range (0,int(num_player)):
    player.append(x)

# Randomly selecting a player
turn=random.choice(player)
win=False
while win==False: #Iterating the loop till any player wins or the game is a tie
    count=0
    print("Player ",turn+1," chance")
    loc=input('Enter Checker column: ')
    location=[*loc]
    
#         Checks for invalid user input
        
    if len(location)>1: 
        
        print('Invalid column entered\nGame Ended')
        sys.exit()
        
#         Check for invalid column
    elif (ord(location[0]) not in range(0+65,NUM_COLS+65) ) :
        
        print('Invalid column entered\nGame Ended')
        sys.exit()
    
    elif (ord(location[0]) in range(0+65,NUM_COLS+65)) :
        
        for row in range(NUM_ROWS):
            if board[row][ord(location[0])-65]!=' ':
                count=count+1
        if count==NUM_ROWS:
            print('Entire column is filled\nOops!You missed a chance\n\n')
            turn=(turn+1)%len(player)
            continue
        
        # Putting a checker if column has space 
        board[(NUM_ROWS-1)-count][ord(location[0])-65]=checkers[turn]
        # Altering turn
        turn=(turn+1)%len(player) 
        print_board()
        # Checking for a win
        for x in player:
            if check_win(board,checkers[x])==True:
                print("Player ",x+1,' wins')
                win=True
        # Checking for a draw
        if check_draw(board)==True:
            sys.exit()
        






