filename = 'data.txt'

line = 'Animals:'
species = ['Elephant', 'Monkey', 'Tiger', 'Lion', 'Horse']


def write1():
    with open(filename, 'w') as file:
        file.write(line + "\n")

        for animal in species:
            file.write(animal + '\n')


def read1():
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip() + " ", end='')


def append1():
    with open(filename, 'a') as file:
        file.write('\n')
        file.write("Tu bedzie strona internetowa")


def append2():
    with open(filename, 'a') as file:
        file.write('\n')
        file.write(input("Podaj swoja ulubiona strone internetowa"))


def read2():
    with open(filename, 'r') as file:
        for line in file:
            print(line)

try:
    read1()
    write1()
    append1()
    append2()
    read2()
except FileNotFoundError:
    print("Nieprawidlowy plik")
