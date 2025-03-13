from random import randint

from brain_games.scripts.brain_games_engine import brain_engine


def is_even_game():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    
    def get_expression():
        expression = randint(1, 101)
        return expression
    
    def get_statement(expression):
        statement = (expression % 2 == 0)
        return statement
    
    def correct_answer(expression):
        return ((get_statement(expression) and 'yes')
                 or (not get_statement(expression) and 'no'))
    brain_engine(task, get_expression, correct_answer)


def main():
    #  brain_engine(is_even_game, task, guessed_expression, correct_answer)
    is_even_game()


if __name__ == '__main__':
    main()
