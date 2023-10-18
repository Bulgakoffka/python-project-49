answer = 0
canswer = 0
user_name = '...'


def lose(answer, canswer, user_name):
    print(f"""'{answer}' is wrong answer ;(. Correct answer was '{canswer}'.
    Let's try again, {user_name}!""")


def main():
    lose(answer, canswer, user_name)


if __name__ == '__main__':
    main()
