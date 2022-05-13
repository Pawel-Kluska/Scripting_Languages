import CovidService
import Natural_Language_Translator

obj = CovidService.CovidService("Covid.txt")

# data1 = obj.evaluate_by_date(23, 'listopad', 'Afghanistan', 'cases', False, 'cases', False)
# print(data1)

# day month teritory cases/deaths sum sort desc

# data1 = obj.evaluate_by_date(None, None, 'Asia', 'cases', True, 'cases', True)
# print(data1)

# day1

# day1, month1, day2, month2, teritory, case_or_death, if_sum, order, if_desc

# data1 = obj.evaluate_by_interval(1, 'listopad', 25, 'listopad', 'Afghanistan', 'cases', False, 'cases', True)
# print(data1)


# show sum/list of cases/deaths in territory (for nr month) / (between day1 month1 and day2 month2)
# order by cases/deaths/day desc/asc


service = CovidService.CovidService('Covid.txt')
t = Natural_Language_Translator.Translator(service)
result = t.translate('show list of cases in Asia for 1 April order by cases desc')
print(result)
