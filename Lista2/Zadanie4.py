import random

nr_of_numbers = 6
list_of_numbers = list(range(50))

random_numbers = random.sample(list_of_numbers, nr_of_numbers)

print(random_numbers)

