is_not_ending = True

print("Witam w moim programie")

list_of_files = []
list_of_extensions = []

while is_not_ending:
    name = input("Podaj plik z rozszerzeniem: ")
    list_of_files.append(name)
    if name.split(".")[1] not in list_of_extensions:
        list_of_extensions.append(name.split(".")[1])
    if input("Czy chcesz wyjsc z programu? (Wpisz q)") == 'q':
        is_not_ending = False

list_of_files.sort()

list_of_types_ext = [[] for element in range(len(list_of_extensions))]


for elem in list_of_files:
    index = list_of_extensions.index(elem.split(".")[1])
    list_of_types_ext[index].append(elem)

print(list_of_types_ext)
dictionary = dict()


for element in list_of_types_ext:
    for i in element:
        if i.split(".")[1] not in dictionary:
            dictionary[i.split(".")[1]] = 0

        dictionary[i.split(".")[1]] += 1

print(dictionary)

template = "{0:8s} {1:6d}"
print("{0:8s} {1:>6s}".format("Rozszerzenie", "ilosc"))
for key, value in dictionary.items():
    print(template.format(key, value))