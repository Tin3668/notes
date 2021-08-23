import os
# home function


def home():
    with open("txt files\\home.txt", 'r') as f:
        print(f.read())


def next():
    print('')
    print('=' * 59)
    print('')


def list():
    with open("txt files\\list.txt", 'r') as f:
        print(f.read())


def add(words):
    with open("txt files\\list.txt", 'a') as f:
        f.write(words + '\n')


def delete(delwords):
    with open("txt files\\list.txt", "r") as f:
        lines = f.readlines()

    with open("txt files\\list.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != delwords:
                f.write(line)


run = True

while run:
    home()
    INPUT = input("> ").lower()

    if INPUT == "list":
        list()
    elif INPUT == 'add':
        WORDS = input('add: ').lower()
        add(WORDS)
    elif INPUT == 'delete':
        DEL = input('del: ').lower()
        delete(DEL)
    elif INPUT == 'quit':
        run = False
