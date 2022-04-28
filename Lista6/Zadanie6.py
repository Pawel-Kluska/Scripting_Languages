from Lista6.Zadanie5 import Person

file = 'Persons.txt'

list_of_persons = []

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        person = Person(line.strip())
        list_of_persons.append(person)

print(list_of_persons)
