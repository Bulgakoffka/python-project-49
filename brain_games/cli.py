from prompt import string


def welcome_user():
	name = string('May I have your name? ')
	print(f'Hello, {name}!')


if __name__ == '__main__':
	welcome_user()
