from timeit import default_timer as timer


def read_all_cases():
    start = timer()
    list_c = []
    with open('Covid.txt', 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            data = line.split("\t")
            list_c.append((data[6], int(data[3]), int(data[2]), int(data[1]), int(data[5]), int(data[4])))
    end = timer()
    print("Read all cases {} ".format((end - start) * 1000))
    return list_c


def get_dict_date(allCases):
    start = timer()
    dict_d = {}
    for case in allCases:
        key = (case[1], case[2], case[3])
        if key in dict_d:
            dict_d[key].append((case[0], case[4], case[5]))
        else:
            dict_d[key] = [(case[0], case[4], case[5])]
    end = timer()
    print("Read dictionary by date {} ".format((end - start) * 1000))
    return dict_d


def get_dict_country(allCases):
    start = timer()
    dict_c = {}
    for case in allCases:
        key = case[0]
        if key in dict_c:
            dict_c[key].append((case[1], case[2], case[3], case[4], case[5]))
        else:
            dict_c[key] = [(case[1], case[2], case[3], case[4], case[5])]
    end = timer()
    print("Read dictionary by country {} ".format((end - start) * 1000))
    return dict_c