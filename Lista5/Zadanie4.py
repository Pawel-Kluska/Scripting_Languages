from Lista5.Zadanie1 import read_all_cases, get_dict_date, get_dict_country
from timeit import default_timer as timer

all_cases = read_all_cases()
by_date = get_dict_date(all_cases)
by_country = get_dict_country(all_cases)


def for_date_country_a(year, month, day, country):
    start = timer()
    d = 0
    c = 0
    for i in all_cases:
        name, year_, month_, day_, death, case = i
        if name == country and (year_, month_, day_) == (year, month, day):
            c += case
            d += death
    end = timer()
    print("For date country a: {} ".format((end - start) * 1000))
    return c, d


def for_date_country_d(year, month, day, country):
    start = timer()
    d = 0
    c = 0
    cases = by_date[(year, month, day)]
    for i in cases:
        name, death, case = i
        if name == country:
            c += case
            d += death
    end = timer()
    print("For date country d: {} ".format((end - start) * 1000))
    return c, d


def for_date_country_c(year, month, day, country):
    start = timer()
    d = 0
    c = 0
    countries = by_country[country]
    for i in countries:
        year_, month_, day_, death, case = i
        if (year, month, day) == (year_, month_, day_):
            c += case
            d += death
    end = timer()
    print("For date country c: {} ".format((end - start) * 1000))
    return c, d


print(for_date_country_a(2020, 11, 23, 'Afghanistan'))
print(for_date_country_c(2020, 11, 23, 'Afghanistan'))
print(for_date_country_d(2020, 11, 23, 'Afghanistan'))
