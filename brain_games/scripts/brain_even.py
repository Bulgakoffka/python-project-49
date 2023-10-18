#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.misc import lose

user_name = welcome_user()


def check(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def ask_question():
    number = randint(1, 30)
    print('Question: ' + str(number))
    guess_answer = input('Your answer: ')
    return number, guess_answer


def is_even():
    win_count = 0
    while win_count != 4:
        if win_count == 3:
            print('Congratulations, ' + user_name + '!')
            break
        number, guess_answer = ask_question()
        if guess_answer == 'yes' and number % 2 == 0:
            print('Correct!')
            win_count += 1
        elif guess_answer == 'no' and number % 2 != 0:
            print('Correct!')
            win_count += 1
        elif guess_answer != 'yes' and guess_answer != 'no':
            lose(guess_answer, check(number), user_name)
            win_count = 0
            break
        else:
            lose(guess_answer, check(number), user_name)
            break


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even()


if __name__ == '__main__':
    main()
