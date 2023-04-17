from art import logo
from art import vs
from game_data import data
import os
import random

def start_game():
    def format_data(account):
        account_name = account['name']
        account_descr = account['description']
        account_country = account['country']
        return f'{account_name}, a {account_descr}, from {account_country}'

    def check_answer(guess, a_followers, b_followers):
        if a_followers > b_followers:
            return guess == 'a'  
        else:
            return guess == 'b'

    score = 0
    game_should_continue = True

    while game_should_continue:
        account_a = random.choice(data)
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        
        print(logo)
        print(f'Current score: {score}')
        print(f'Compare A: {format_data(account_a)}')

        print(vs)

        print(f'Compare B: {format_data(account_b)}')

        guess = input('Who was more followers? Type "A" or "B": ').lower()

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f'You\'re right! Current score: {score}')
            os.system('cls')
        else:
            game_should_continue = False
            print(f'Sorry, that\'s wrong. Final score: {score}')
            if input('Do you return a "HigherLower" game? "Y" or "N": ').lower() == 'y':
                os.system('cls')
                start_game()
            else:
                os.system('cls')

if input('Do you started "HigherLower" game? "Y" or "N": ').lower() == 'y':
    os.system('cls')
    start_game()
