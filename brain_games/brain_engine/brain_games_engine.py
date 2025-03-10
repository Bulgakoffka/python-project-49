from prompt import string
from brain_games.games.brain_games import greeting
from brain_games.cli import welcome_user


def brain_engine(task, get_expression, correct_answer):
    name = welcome_user()
    win_count = 0
    print(task)
    while win_count < 3:
        cycle_gexp = get_expression()
        print(cycle_gexp)
        user_answer = string('Your answer: ')
        if str(user_answer) == str(correct_answer(cycle_gexp)):
            print('Correct!')
            win_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was {correct_answer(cycle_gexp)}")
            win_count = 0
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')







if __name__ == '__main__':
    None