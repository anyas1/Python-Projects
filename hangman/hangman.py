import random
from words import words
import string

def select_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.Upper()

def hangman():
    word = select_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already guessed that letter. Please try again.')

    else:
        print('Invalid character. Try again.')

    return hangman
