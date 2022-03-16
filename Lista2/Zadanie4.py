import random

nr_of_numbers = 6
list_of_numbers = list(range(50))

random_numbers = []

for i in range(nr_of_numbers):
    number = random.choice(list_of_numbers)
    list_of_numbers.remove(number)
    random_numbers.append(number)

print(random_numbers)

