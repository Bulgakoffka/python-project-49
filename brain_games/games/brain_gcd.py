from math import gcd
from random import randint

from brain_games.scripts.brain_games_engine import brain_engine


def gcd_game():
    task = 'Find the greatest common divisor of given numbers.'
    
    def get_expression():
        global int1, int2
        int1 = randint(1, 51)
        int2 = randint(1, 51)
        expression = f'{int1} {int2}'
        return expression
    
    def correct_answer(expression):
        int1, int2 = expression.split()
        return gcd(int(int1), int(int2))

    brain_engine(task, get_expression, correct_answer)


def main():
    gcd_game()


if __name__ == '__main__':
    main()