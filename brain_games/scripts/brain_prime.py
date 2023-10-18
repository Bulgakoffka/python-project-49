#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.misc import lose

user_name = welcome_user()


def is_prime(number):
    check = 0
    for i in range(2, (number - 1)):
        if number % i == 0:
            check += 1
    if check > 0:
        return 'no'
    else:
        return 'yes'


def brain_prime():
    win_count = 0
    while win_count != 4:
        if win_count == 3:
            print('Congratulations, ' + user_name + '!')
            break
        guess_number = randint(1, 30)
        print('Question: ' + str(guess_number))
        guess_answer = input('Your answer: ')

        if guess_answer == 'yes':
            if is_prime(guess_number) == 'yes':
                print('Correct!')
                win_count += 1
            else:
                lose(guess_answer, is_prime(guess_number), user_name)
                win_count = 0
                break
        if guess_answer == 'no':
            if is_prime(guess_number) == 'no':
                print('Correct!')
                win_count += 1
            else:
                lose(guess_answer, is_prime(guess_number), user_name)
                break
        if guess_answer != 'yes' and guess_answer != 'no':
            lose(guess_answer, is_prime(guess_number), user_name)
            win_count = 0
            break


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime()


if __name__ == '__main__':
    main()
