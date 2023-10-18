#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.misc import lose


user_name = welcome_user()


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def delenie(a, b):
    return a / b


def umnozhenie(a, b):
    return a * b


def randnumber():
    a = randint(1, 30)
    return a


def randmath():
    win_count = 0
    while win_count != 4:
        choice = randint(1, 3)
        a, b = randnumber(), randnumber()
        if win_count == 3:
            print('Congratulations, ' + user_name + '!')
            break
        match choice:
            case 1:
                print('Question: ' + f'{a} * {b}')
                answer = input('Your answer: ')
                try:
                    if int(answer) == int(umnozhenie(a, b)):
                        print('Correct!')
                        win_count += 1
                    else:
                        lose(answer, umnozhenie(a, b), user_name)
                        break
                except ValueError:
                    lose(answer, umnozhenie(a, b), user_name)
                    win_count = 0
                    break
            case 2:
                print('Question: ' + f'{a} - {b}')
                answer = input('Your answer: ')
                try:
                    if int(answer) == int(minus(a, b)):
                        print('Correct!')
                        win_count += 1
                    else:
                        lose(answer, minus(a, b), user_name)
                        break
                except ValueError:
                    lose(answer, minus(a, b), user_name)
                    win_count = 0
                    break
            case 3:
                print('Question: ' + f'{a} + {b}')
                answer = input('Your answer: ')
                try:
                    if int(answer) == int(plus(a, b)):
                        print('Correct!')
                        win_count += 1
                    else:
                        lose(answer, plus(a, b), user_name)
                        win_count = 0
                        break
                except ValueError:
                    lose(answer, plus(a, b), user_name)
                    win_count = 0
                    break


def main():
    print('What is the result of the expression?')
    randmath()


if __name__ == '__main__':
    main()
