from random import choice, randint

from brain_games.scripts.brain_games_engine import brain_engine


def calc_game():
    task = 'What is the result of the expression?'

    def get_expression():
        operator_list = ['+', '-', '*']
        int1 = randint(1, 51)
        int2 = randint(1, 51)
        global expression
        expression = f'{int1} {choice(operator_list)} {int2}'
        return expression
    
    def correct_answer(exp):
        return eval(exp)
    brain_engine(task, get_expression, correct_answer)


def main():
    calc_game()


if __name__ == '__main__':
    main()
