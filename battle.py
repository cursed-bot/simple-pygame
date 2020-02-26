# a two to three player changable game *i might not be able to 
# work a three player game* 

gamelog = open('game_log.txt',"a") # creates or opens the game log to store the name of all players

p1name = '' # this will set the player name variables 
p2name = ''
p3name = ''

import random # depending on the game i'm playing i will import the game code here.
import dice_game 

print('how many people are playing today?')
print('(type either p2 or p3*not ready yet, you will get an error* and press enter to select or type end to exit the game.)')
while True:
    playercount = input() #this will tell it what game mode to play.

    if playercount == 'p2':
        print('player 1, please type your name with a space at the end') # this allows it says the players name
        p1name = input()
        gamelog.write(p1name)
        print('player 2, please type your name with a space at the end')
        p2name = input()
        gamelog.write(p2name)
        dice_game.p2(p1name, p2name) #remeber to change the game importer on this line when switching games

    elif playercount == '':
        print('player 1, please type your name') # this allows it says the players name
        p1name = input()
        gamelog.write(p1name)
        print('player 2, please type your name')
        p2name = input()
        gamelog.write(p2name)
        print('player 3, please type your name')
        p3name = input()
        gamelog.write(p3name)
        dice_game.p3(p1name, p2name, p3name) #remeber to change the importer on this line when switching games
    
    elif playercount == 'end':
        print('thanks for playing, play again soon!')
        gamelog.close()
        break

    elif playercount == "if you're 555 then i'm":
        print('6(SIC)6') 

    else:
        print('that is not a valid player count, please try again')
        print('type either p2 or p3 or end and press enter')