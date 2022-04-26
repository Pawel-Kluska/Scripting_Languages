from Lista5.Zadanie1 import read_all_cases, get_dict_date, get_dict_country
from timeit import default_timer as timer

all_cases = read_all_cases()
by_date = get_dict_date(all_cases)
by_country = get_dict_country(all_cases)


def measure_time3(fun, country):
    start = timer()
    fun(country)
    end = timer()
    print("For date a: {} ".format((end - start) * 1000))


def for_country_a(country):
    d = 0
    c = 0
    for i in all_cases:
        name, year_, month_, day_, death, case = i
        if name == country:
            c += case
            d += death

    return c, d


def for_country_d(country):
    c = 0
    d = 0
    for values in by_date.values():
        for i in values:
            name, death, case = i
            if name == country:
                c += case
                d += death

    return c, d


def for_country_c(country):
    c = 0
    d = 0
    countries = by_country[country]
    for i in countries:
        c += i[4]
        d += i[3]

    return c, d


print(for_country_a('Afghanistan'))
print(for_country_c('Afghanistan'))
print(for_country_d('Afghanistan'))

measure_time3(for_country_a, 'Afghanistan')
measure_time3(for_country_c, 'Afghanistan')
measure_time3(for_country_d, 'Afghanistan')
