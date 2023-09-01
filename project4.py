# Guess the number game
import random

min_value = 1
max_value = 20
random_number = random.randint(min_value, max_value)


input("To begin the game, press Enter")
print('--------------')

while True:
    guess = input('Select a number 1-20 ')
    if guess.isdigit():
        guess = int(guess)
        if guess < min_value or guess > max_value:
            print('Number out of range. Select a number 1-20')
        elif guess > random_number:
            guess = int(guess)
            print("Too high")
        elif guess < random_number:
            guess = int(guess)
            print("Too low")
        elif guess == random_number:
            break
    else:
        print('Invalid number. Try again')

print('--------------')
print('Nice work! The correct number was', random_number )