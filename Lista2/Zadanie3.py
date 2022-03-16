import random

nr_of_rounds = 2
nr_of_throws = 4
list_of_sums = []

for i in range(nr_of_rounds):
    list_of_sums.append(0)
    for j in range(nr_of_throws):
        throw = random.randint(1,6)
        list_of_sums[i] += throw

print(list_of_sums)
best_round = max(list_of_sums)
print("{0:d} byla najlepsza runda ".format(list_of_sums.index(int(best_round)) + 1))
print("Sumarycznie wyrzucono wtedy {0:d} ".format(best_round))


