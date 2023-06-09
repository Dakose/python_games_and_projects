from art import logo
from random import randint
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns -1
    else:
        print(f'You got it! The answer was: {answer}.')

def set_dificulty():
    level = input('Chose a difficulty. type "ease" or "hard": ')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print('Welcome to the Number Guessing Game')
    print('I`m thinking of a number between 1 and 100.')
    answer = randint(0, 100)
    # help
    print(f'Psst, the correct answer is {answer}')

    turns = set_dificulty()
    guess = 0
    while guess != answer:
        print(f'You hav e {turns} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You`ve out of guesses. you lose.')
            return
        elif guess != answer:
            print('Guess again.')

while input('Do you want to play a game of Blackjack? Type "y" or "n": ') == 'y':
    os.system('cls')
    game()