#Rock paper scissors :)

import random

def is_win(player, opponent):
    if(player=='rock' and opponent=='scissors') or (player=='scissors' \
    and opponent=='paper') or (player=='paper' and opponent=='rock'):
        return True

def is_lose(player, opponent):
    if(opponent=='rock' and player=='scissors') or (opponent=='scissors' \
    and player=='paper') or (opponent=='paper' and player=='rock'):
        return True
    
def play():
    computer = random.choice(['rock','paper','scissors'])

    while True:
        user = input('Select rock, paper, or scissors ')
        if user == 'rock' or user == 'paper' or user == 'scissors':
            if user == computer:
                print('\nIts a tie, the computer also chose', computer)
                user = input('Would you like to play again? (y/n)\n')  
                if user == 'y':
                    return play()
                else:
                    break

            if is_win(user, computer):
                print('\nYou won, the computer chose', computer)  
                user = input('Would you like to play again? (y/n)\n')  
                if user == 'y':
                    return play()
                else:
                    break
        
            if is_lose(user, computer):
                print('\nYou lost, the computer chose', computer)
                user = input('Would you like to play again? (y/n)\n')  
                if user == 'y':
                    return play()
                else:
                    break
        else:
            print('Invalid input, try again.')

print(play())


        