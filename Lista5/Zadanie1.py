from timeit import default_timer as timer


def measure_time(funct):
    start = timer()
    funct()
    end = timer()
    print("Time measured: {} ".format((end - start) * 1000))


def read_all_cases():
    list_c = []
    with open('Covid.txt', 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            data = line.split("\t")
            list_c.append((data[6], int(data[3]), int(data[2]), int(data[1]), int(data[5]), int(data[4])))

    return list_c


def get_dict_date(allCases):
    dict_d = {}
    for case in allCases:
        key = (case[1], case[2], case[3])
        if key in dict_d:
            dict_d[key].append((case[0], case[4], case[5]))
        else:
            dict_d[key] = [(case[0], case[4], case[5])]

    return dict_d


def get_dict_country(allCases):
    dict_c = {}
    for case in allCases:
        key = case[0]
        if key in dict_c:
            dict_c[key].append((case[1], case[2], case[3], case[4], case[5]))
        else:
            dict_c[key] = [(case[1], case[2], case[3], case[4], case[5])]

    return dict_c


def read_all_cases_mod():
    wartosc = -1
    while wartosc < 0 or wartosc > 12:
        wartosc = int(input("Podaj liczbe elementow krotki: "))

    list_c = []
    with open('Covid.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.split("\t")
            initial_tuple = tuple(data)
            sliced_tuple = initial_tuple[:wartosc]
            list_c.append(sliced_tuple)

    return list_c


#list_all_cases_mod = read_all_cases_mod()

#for i in list_all_cases_mod:
 #   print(i)


