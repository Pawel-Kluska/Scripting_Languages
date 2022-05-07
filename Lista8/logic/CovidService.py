from Lista8.logic import CovidData


class CovidService:
    __month_dict = {'January': '01',
                    'February': '02',
                    'March': '03',
                    'April': '04',
                    'May': '05',
                    'June': '06',
                    'July': '07',
                    'August': '08',
                    'September': '09',
                    'October': '10',
                    'November': '11',
                    'December': '12'}

    def __init__(self, filename):
        self.data = CovidData.Covid_Data(filename)

    def find_by_month(self, month):
        dict_date = self.data.get_by_date_dict()
        result = []
        month_n = int(CovidService.__month_dict[month])
        for key, value in dict_date.items():
            if key[1] == month_n:
                for i in value:
                    result.append((i[0],) + key + i[1:])
        return result

    def find_by_month_day(self, month, day):
        month_n = int(CovidService.__month_dict[month])
        dict_date = self.data.get_by_date_dict()
        result = []
        data = dict_date[(2020, month_n, day)]
        for i in data:
            result.append((i[0],) + (2020, month_n, day) + i[1:])
        return result

    def find_by_interval(self, month1, day1, month2, day2):
        result = []
        month_1_n = int(CovidService.__month_dict[month1])
        month_2_n = int(CovidService.__month_dict[month2])
        dict_date = self.data.get_by_date_dict()
        for key, value in dict_date.items():
            if month_1_n <= key[1] <= month_2_n and day1 <= key[2] <= day2:
                for i in value:
                    result.append((i[0],) + key + i[1:])
        return result

    def find_by_country(self, country):
        dict_country = self.data.get_by_country_dict()
        result = []
        for i in dict_country[country]:
            result.append((country,) + i)
        return result

    def find_by_continent(self, continent):
        dict_continent = self.data.get_by_continent_dict()
        result = []
        for i in dict_continent[continent]:
            result.append((i[3],) + i[0:3] + (continent,) + i[4:])
        return result

    def check_if_continent(self, continent):
        if continent in self.data.get_all_continents():
            return True
        else:
            return False

    def check_if_country(self, country):
        if country in self.data.get_all_countries():
            return True
        else:
            return False

    def get_sum(self, data):
        cases = 0
        deaths = 0
        for i in data:
            cases += i[6]
            deaths += i[5]
        return cases, deaths

    def sort_data(self, data, order, if_desc):
        if order == "date":
            result = sorted(data, key=lambda tup: (tup[1], tup[2]))
        elif order == "cases" or "deaths":
            result = sorted(data, key=lambda tup: tup[3])
        else:
            raise ValueError("Wrong input")
        if if_desc:
            result.reverse()
        return result

    def get_final_list(self, data, case_or_death):
        result = []
        if case_or_death == "cases":
            for record in data:
                result.append((record[1], record[2], record[3], record[6]))
        elif case_or_death == "deaths":
            for record in data:
                result.append((record[1], record[2], record[3], record[5]))
        return result

    def evaluate_by_date(self, day, month, teritory, case_or_death, if_sum, order, if_desc):
        result_list = []
        if day and month is not None:
            result_list = self.find_by_month_day(month, day)
        elif day is None and month is not None:
            result_list = self.find_by_month(month)

        return self.evaluate_rest(result_list, teritory, case_or_death, if_sum, order, if_desc)

    def evaluate_by_interval(self, day1, month1, day2, month2, teritory, case_or_death, if_sum, order, if_desc):

        result_list = self.find_by_interval(month1, day1, month2, day2)

        if not result_list:
            raise ValueError("Wrong interval")

        return self.evaluate_rest(result_list, teritory, case_or_death, if_sum, order, if_desc)

    def evaluate_rest(self, result_list, teritory, case_or_death, if_sum, order, if_desc):

        if self.check_if_continent(teritory):
            teritory_list = self.find_by_continent(teritory)
        elif self.check_if_country(teritory):
            teritory_list = self.find_by_country(teritory)
        else:
            raise ValueError("Wrong data")

        if result_list:
            result_list = list(set(result_list).intersection(set(teritory_list)))
        else:
            result_list = teritory_list

        if if_sum and case_or_death == 'cases':
            return 'Sum of cases for {}: {}'.format(teritory, self.get_sum(result_list)[0])
        elif if_sum and case_or_death == 'deaths':
            return 'Sum of deaths for {}: {}'.format(teritory, self.get_sum(result_list)[1])
        else:
            result_list = self.get_final_list(result_list, case_or_death)

        if order is not None:
            result = self.sort_data(result_list, order, if_desc)

        str_result = '{} for {} \n'.format(case_or_death.capitalize(), teritory)
        for i in result:
            str_result += '{}/{}/{} - {} {} \n'.format(i[2], i[1], i[0], i[3], case_or_death)

        return str_result
