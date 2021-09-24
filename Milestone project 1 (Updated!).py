#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Gamecode
initialboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def displayboard (list):
    print (list[1]+ '|' + list[2] + '|' + list[3])
    print('-----')
    print (list[4]+ '|' + list[5] + '|' +list[6])
    print('-----')
    print (list[7]+ '|' + list[8] + '|' +list[9])
    
displayboard(initialboard)

def instructions ():
    print('Welcome to tic-tac-toe!')
    print('There are 2 players. Each player will first choose their desired symbol.')
    print('The game will select a player at RANDOM to start first')
    print('Game will end when a player wins or the board is full')
    
instructions()

def keepplaying():
    global game_status,board
    game_status= 'Yummy'
    while game_status not in ['On','Off']:
        response = input("Want to keep on playing? Please select either Y or N: ")
        
        if response == 'Y':
            game_status = 'On'
            board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
           
            return game_status
        
        elif response == 'N':
            game_status = 'Off'
            return game_status

keepplaying()

def playersymbolchoice():
    global player1symbol, player2symbol
    player1symbol = "Homosapiens"
    while player1symbol not in ['$','@']:
        player1symbol = input('Player 1, please select your symbol: $ OR @: ')
        if player1symbol == '$':
            player2symbol = '@'
            print("Player 1 has selected $ and player 2 has been assigned @ as his/her symbol")

        elif player1symbol == '@':
            player2symbol = '$'
            print("Player 1 has selected @ and player 2 has been assigned $ as his/her symbol")
        
from random import randint
def cointoss():
    global turn,numberA,numberB
    numberA = randint(1,2)
    numberB = str(numberA)
    turn = 'Player '+ numberB
    print('Player ' + numberB + ' will start first')
    
def playerchoice():
    global playeroption
    playeroption = 'Marine'
    while playeroption not in range(1,10):
        try:
            playeroption = int(input("Please select a number between 1 and 10: "))
        
        except ValueError:
            print('Sorry that was NOT an integer! Please try again')
            
        
            
            
        
    
def spacecheck(playeroption):
    global freespace
    if board[playeroption] == ' ':
        freespace = True
        print('Updating board...')
        
    elif board[playeroption] != ' ':
        freespace = False
        print('That space is already taken! Please try again') 
        
        
def updateboard(board, symbol, playeroption):
    if freespace == True:
        board[playeroption] = symbol
    elif freespace== False:
        pass
    

def victorycheck(board,mark):
    if freespace == True:
        return(board[1]== board[4]== board[7] == mark 
        or board[1]==board[2]==board[3]== mark 
        or board[4]==board[5]==board[6]== mark 
        or board[7]==board[8]==board[9]== mark
        or board[7]==board[5]==board[3]== mark 
        or board[1]==board[5]==board[9]== mark 
        or board[2]== board[5]== board[8] == mark
        or board[3]== board[6]== board[9] == mark)
    
    elif freespace == False:
        pass
         
playersymbolchoice()
cointoss()
while game_status == 'On':

    if turn == 'Player 1':
        symbol = player1symbol
        playerchoice()
        spacecheck(playeroption)
        updateboard(board, symbol, playeroption)
        displayboard(board)
        victorycheck(board,symbol)
        if victorycheck(board,symbol) == True:
            print("Player 1 has won!!!")
            keepplaying()
                
        elif victorycheck!=True and freespace == False:
            continue
            
        elif victorycheck!=True:
            turn = 'Player 2'
            
                
    if turn == 'Player 2':
        symbol = player2symbol
        playerchoice()
        spacecheck(playeroption)
        updateboard(board, symbol, playeroption)
        displayboard(board)
        victorycheck(board,symbol)
        if victorycheck(board,symbol)== True:
            print("Player 2 has won!!!")
            keepplaying()
            
        elif victorycheck!=True and freespace == False:
            continue
            
        elif victorycheck!=True:
            turn = 'Player 1'

if game_status == 'Off':
    print("Thank you for playing!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




