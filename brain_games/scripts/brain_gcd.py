from random import randint
from cli import welcome_user

def randnumber():
    a = randint(1, 30)
    return a

user_name = welcome_user()


# user_name = 'Stephen'

def calc(a, b):
    if a < b:
        for i in range(1, b):
            if a % i == 0 and b % i == 0:
                c = i
    else:
        for i in range(1, a):
            if a % i == 0 and b % i == 0:
                c = i
    return c



def nod():
    win_count = 0
    while win_count != 4:
        if win_count == 3:
            print('Congratulations, ' + user_name)
            break
        a, b = randnumber(), randnumber()
        print(f'Question: {a} {b}')
        answer = input('Your answer: ')
        if int(answer) == int(calc(a, b)):
            print('Correct!')
            win_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{calc(a, b)}'. \n Let's try again, {user_name}!")
            win_count = 0
            break



def main():
    print('Find the greatest common divisor of given numbers.')
    nod()

if __name__ == '__main__':
    main()
