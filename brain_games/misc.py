from random import randint

answer = 0
canswer = 0
user_name = '...'
win_count = 0


def lose(answer, canswer, user_name):
    print(f"""'{answer}' is wrong answer ;(. Correct answer was '{canswer}'.
    Let's try again, {user_name}!""")


def ask_question():
    number = randint(1, 30)
    print('Question: ' + str(number))
    guess_answer = input('Your answer: ')
    return number, guess_answer


def main():
    lose(answer, canswer, user_name)


if __name__ == '__main__':
    main()
