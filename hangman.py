# Hangman project by Dheeraj Somashekar 
# 2/24/24

import random  # random module 
from car_companies import car_companies   # import list of car companies
import string  


def get_valid_word(cars):
    randomCar = random.choice(cars)  # randomly chooses something from the list
    while '-' in cars or ' ' in cars:
        randomCar = random.choice(cars)

    return randomCar.upper()


def hangman():
    word = get_valid_word(car_companies)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7   # 7 lives

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
 
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)           # Add used letter to used_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)   # remove the word that the user guessed 
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        
        print('You died! The word was', word)
    else:
        print('Good job! You guessed the word', word)


if __name__ == '__main__':
    hangman()
