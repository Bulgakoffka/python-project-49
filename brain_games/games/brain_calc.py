from random import randint, choice
from brain_games.brain_engine.brain_games_engine import brain_engine


def calc_game():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    def get_expression():
        int1 = randint(1, 51)
        int2 = randint(1, 51)
        global expression
        expression = f'{int1} {choice('+', '-', '*')} {int2}'
    def correct_answer():
        return eval(expression)
    brain_engine(task, get_expression, correct_answer)





def main():
    is_even_game()


if __name__ == '__main__':
    main()
