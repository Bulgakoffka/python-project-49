#!/usr/bin/env python3

def welcome_user():
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def greet():
    print('Welcome to the Brain Games!')

def main():
    greet()
    welcome_user()

if __name__ == '__main__':
    main()

