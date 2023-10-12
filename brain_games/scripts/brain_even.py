from random import randint
from cli import welcome_user

user_name = welcome_user()

def is_even():
    win_count = 0
    while win_count != 3:
        number = randint(1, 30)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question: ' + str(number))
        guess_answer = input('Your answer: ')
        if guess_answer == 'yes':
            if number % 2 == 0:
                print('Correct!')
                win_count += 1
            else:
                print(f"'{guess_answer}' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, {user_name}!")
                win_count = 0
        if guess_answer == 'no':
            if number % 2 != 0:
                print('Correct!')
                win_count += 1
            else:
                print(f"'{guess_answer}' is wrong answer ;(. Correct answer was 'yes'. \n Let's try again, {user_name}!")
                win_count = 0
        if guess_answer != 'yes' and guess_answer != 'no':
            print(f"'{guess_answer}' is wrong answer ;(. \n Let's try again, {user_name}!")
            win_count = 0
        if win_count == 3:
            print('Congratulations, ' + user_name)

is_even()
