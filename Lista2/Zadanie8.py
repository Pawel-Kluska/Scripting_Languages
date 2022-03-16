import os

filename = 'data.txt'

line = 'Animals:'

species = ['Elephant', 'Monkey', 'Tiger', 'Lion', 'Horse']

with open('data.txt', 'w') as file:
    file.write(line + "\n")

    for animal in species:
        file.write(animal + '\n')

with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip() + " ", end='')

with open('data.txt', 'a') as file:
    file.write('\n')
    file.write("Tu bedzie strona internetowa")

with open('data.txt', 'a') as file:
    file.write('\n')
    file.write(input("Podaj swoja ulubiona strone internetowa"))

with open('data.txt', 'r') as file:
    for line in file:
        print(line)

