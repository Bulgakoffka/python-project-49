from prompt import string
from random import randint
from brain_games.scripts.brain_games import greeting
from brain_games.cli import welcome_user


def is_even_game():
    name = welcome_user()
    win_count = 0
    while win_count < 3:
        guessed_number = randint(1, 101)
        task = 'Answer "yes" if the number is even, otherwise answer "no".'
        print(f'Question: {guessed_number}')
        user_answer = string('Your answer: ')
        even_checker = (guessed_number % 2 == 0)
        if user_answer == 'yes' and even_checker:
            print(f'Correct!')
            win_count += 1
        elif user_answer == 'no' and not even_checker:
            print(f'Correct!')
            win_count += 1
        else:
            correct_answer = ((even_checker and 'yes') or (not even_checker and 'no'))
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was {correct_answer}")
            win_count = 0
    print(f'Congratulations, {name}!')



def main():
    greeting()
    is_even_game()


if __name__ == '__main__':
    main()
