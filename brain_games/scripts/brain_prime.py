#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.misc import lose, ask_question

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
        guess_number, guess_answer = ask_question()
        if guess_answer == 'yes' and is_prime(guess_answer) == 'yes':
            win_count += 1
        elif guess_answer == 'no' and is_prime(guess_answer) == 'no':
            print('Correct!')
            win_count += 1
        elif guess_answer != 'yes' and guess_answer != 'no':
            lose(guess_answer, is_prime(guess_number), user_name)
            win_count = 0
            break
        else:
            lose(guess_answer, is_prime(guess_number), user_name)
            break


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime()


if __name__ == '__main__':
    main()
