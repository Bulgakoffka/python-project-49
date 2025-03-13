from math import sqrt
from random import randint

from brain_games.scripts.brain_games_engine import brain_engine


def prime_game():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    
    def get_expression():
        global expression
        expression = randint(1, 101)
        return expression
    
    def correct_answer(expression):
        if expression == 1:
            return 'no'
        for i in range(1, int(sqrt(expression))):
            if i != 1 and expression % i == 0:
                return 'no'
        return 'yes'
    brain_engine(task, get_expression, correct_answer)


def main():
    prime_game()


if __name__ == '__main__':
    main()