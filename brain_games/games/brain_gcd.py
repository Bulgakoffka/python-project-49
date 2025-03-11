from random import randint

from brain_games.brain_engine.brain_games_engine import brain_engine


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
        gcd = 1
        int1, int2 = int(int1), int(int2)
        for i in range(1, int1 if int1 > int2 else int2):
            statement = int1 % i == 0 and int2 % i == 0
            if statement:
                gcd = i
        return gcd

    brain_engine(task, get_expression, correct_answer)


def main():
    gcd_game()


if __name__ == '__main__':
    main()