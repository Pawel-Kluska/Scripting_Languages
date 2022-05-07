class Covid_Data:

    def __init__(self, file_name):
        self.__file = file_name
        self.__all_cases = []
        self.__country_dict = {}
        self.__continent_dict = {}
        self.__by_date = {}
        self.read_all_cases()
        self.make_dict_country()
        self.make_dict_continent()
        self.make_dict_date()

    # (nazwa pełna, rok, miesiąc, dzień, kontynent, liczba zgonów, liczba przypadków)
    def read_all_cases(self):
        with open(self.__file, 'r', encoding='utf-8') as file:
            file.readline()
            for line in file:
                data = line.split("\t")
                self.__all_cases.append(
                    (data[6], int(data[3]), int(data[2]), int(data[1]), data[10], int(data[5]), int(data[4])))

    # (rok, miesiąc, dzień)  lista krotek (nazwa pełna, kontynent, liczba zgonów, liczba przypadków)
    def make_dict_date(self):
        for case in self.__all_cases:
            key = (case[1], case[2], case[3])
            if key in self.__by_date:
                self.__by_date[key].append((case[0], case[4], case[5], case[6]))
            else:
                self.__by_date[key] = [(case[0], case[4], case[5], case[6])]

    # nazwa kraju  (rok, miesiąc, dzień, kontynent, liczba zgonów, liczba przypadków)
    def make_dict_country(self):
        for case in self.__all_cases:
            key = case[0]
            if key in self.__country_dict:
                self.__country_dict[key].append((case[1], case[2], case[3], case[4], case[5], case[6]))
            else:
                self.__country_dict[key] = [(case[1], case[2], case[3], case[4], case[5], case[6])]

    # nazwa kontynentu  (rok, miesiąc, dzień, kraj, liczba zgonów, liczba przypadków)
    def make_dict_continent(self):
        for case in self.__all_cases:
            key = case[4]
            if key in self.__continent_dict:
                self.__continent_dict[key].append((case[1], case[2], case[3], case[0], case[5], case[6]))
            else:
                self.__continent_dict[key] = [(case[1], case[2], case[3], case[0], case[5], case[6])]

    def get_all_countries(self):
        country_list = set()
        for i in self.__all_cases:
            country = i[0]
            country_list.add(country)
        return country_list

    def get_all_continents(self):
        continent_list = set()
        for i in self.__all_cases:
            continent = i[4]
            continent_list.add(continent)
        return continent_list

    def get_all_cases(self):
        return self.__all_cases

    def get_by_date_dict(self):
        return self.__by_date

    def get_by_country_dict(self):
        return self.__country_dict

    def get_by_continent_dict(self):
        return self.__continent_dict
