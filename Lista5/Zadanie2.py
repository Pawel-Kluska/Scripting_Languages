from Lista5.Zadanie1 import read_all_cases, get_dict_date, get_dict_country
from timeit import default_timer as timer

all_cases = read_all_cases()
by_date = get_dict_date(all_cases)
by_country = get_dict_country(all_cases)


def measure_time2(fun, year, month, day):
    start = timer()
    fun(year, month, day)
    end = timer()
    print("Time: {} ".format((end - start) * 1000))


def for_date_a(year, month, day):
    all_death = 0
    all_cases = 0
    for i in all_cases:
        name, year_, month_, day_, death, case = i
        if (year, month, day) == (year_, month_, day_):
            all_cases += case
            all_death += death

    return all_cases, all_death


def for_date_d(year, month, day):
    all_cases = 0
    all_death = 0
    ld = by_date[(year, month, day)]

    for i in ld:
        all_cases += i[2]
        all_death += i[1]

    return all_cases, all_death


def for_date_c(year, month, day):
    all_cases = 0
    all_death = 0
    for values in by_country.values():
        for i in values:
            year_, month_, day_, death, case = i
            if (year, month, day) == (year_, month_, day_):
                all_cases += case
                all_death += death

    return all_cases, d


print(for_date_a(2020, 11, 23))
print(for_date_c(2020, 11, 23))
print(for_date_d(2020, 11, 23))

measure_time2(for_date_a, 2020, 11, 23)
measure_time2(for_date_c, 2020, 11, 23)
measure_time2(for_date_d, 2020, 11, 23)
