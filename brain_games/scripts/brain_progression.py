#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user


user_name = welcome_user()


def progression():
    win_count = 0
    while win_count != 4:
        if win_count == 3:
            print('Congratulations, ' + user_name)
            break
        prog = randint(2, 7)
        length = randint(35, 50)
        question = range(1, length, prog)
        question_list = [str(num) for num in question]
        blank = randint(0, (len(question_list) - 1))
        blanked_number = question_list[blank]
        question_list[blank] = '..'
        question = ' '.join(question_list)
        print('Question: ' + question)
        answer = input('Your answer: ')
        try:
            if int(answer) == int(blanked_number):
                        print('Correct!')
                        win_count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{blanked_number}'. \n Let's try again, {user_name}!")
                win_count = 0
                break
        except:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{blanked_number}'. \n Let's try again, {user_name}!")
            win_count = 0
            break




def main():
    print('What number is missing in the progression?')
    progression()


if __name__ == '__main__':
    main()