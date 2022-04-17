from Lista5.Zadanie1 import read_all_cases, get_dict_date, get_dict_country
from timeit import default_timer as timer

all_cases = read_all_cases()
by_date = get_dict_date(all_cases)
by_country = get_dict_country(all_cases)


def for_date_a(year, month, day):
    start = timer()
    d = 0
    c = 0
    for i in all_cases:
        name, year_, month_, day_, death, case = i
        if (year, month, day) == (year_, month_, day_):
            c += case
            d += death
    end = timer()
    print("For date a: {} ".format((end - start) * 1000))
    return c, d


def for_date_d(year, month, day):
    start = timer()
    c = 0
    d = 0
    ld = by_date[(year, month, day)]

    for i in ld:
        c += i[2]
        d += i[1]
    end = timer()
    print("For date d: {} ".format((end - start) * 1000))
    return c, d


def for_date_c(year, month, day):
    start = timer()
    c = 0
    d = 0
    for values in by_country.values():
        for i in values:
            year_, month_, day_, death, case = i
            if (year, month, day) == (year_, month_, day_):
                c += case
                d += death
    end = timer()
    print("For date c: {} ".format((end - start) * 1000))
    return c, d


print(for_date_a(2020, 11, 23))
print(for_date_c(2020, 11, 23))
print(for_date_d(2020, 11, 23))
