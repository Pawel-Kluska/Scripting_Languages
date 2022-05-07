class _RangeError(Exception): pass


class Translator:
    key_words = ['show', 'list', 'sum', 'cases', 'deaths', 'in', 'for', 'order', 'between']

    def __init__(self):
        self.__location = None
        self.__if_sum = None
        self.__deaths_or_cases = None
        self.__day = None
        self.__month = None
        self.__ordering = None
        self.__if_desc = None
        self.__range = None
        self.__service = None
        self.__mode = ''

    def set_service(self, service):
        self.__service = service

    def translate(self, input_string):
        input_ = input_string.split(" ")

        if input_[0] == "show":
            i = 1

            while i < len(input_):
                match input_[i]:
                    case 'list':
                        self.__if_sum = False
                        i += 2
                    case 'sum':
                        self.__if_sum = True
                        i += 2
                    case 'deaths':
                        self.__deaths_or_cases = input_[i]
                        i += 1
                    case 'cases':
                        self.__deaths_or_cases = input_[i]
                        i += 1
                    case 'in':
                        self.__location = input_[i + 1]
                        i += 2
                    case 'for':
                        if isinstance(int(input_[i + 1]), int):
                            self.__day = int(input_[i + 1])
                            self.__month = input_[i + 2]
                            i += 3
                        else:
                            self.__month = input_[i + 1]
                            self.__day = None
                            i += 2
                        self.__mode = 'date'
                    case 'between':
                        if input_[i + 3] == 'and':
                            self.__range = [input_[i + 1], input_[i + 2], input_[i + 4], input_[i + 5]]
                        i += 6
                        self.__mode = 'range'

                    case 'order':
                        self.__ordering = input_[i + 2]
                        if input_[i + 3] == "asc":
                            self.__if_desc = False
                        elif input_[i + 3] == "desc":
                            self.__if_desc = True
                        else:
                            raise ValueError("Wrong command")
                        i += 4
                    case _:
                        raise ValueError("Wrong command")

        else:
            raise ValueError("Wrong command")

        if self.__mode == 'date':
            return self.__service.evaluate_by_date(self.__day, self.__month, self.__location, self.__deaths_or_cases,
                                                   self.__if_sum, self.__ordering, self.__if_desc)
        if self.__mode == 'range':
            return self.__service.evaluate_by_interval(int(self.__range[0]), self.__range[1], int(self.__range[2]),
                                                       self.__range[3], self.__location, self.__deaths_or_cases,
                                                       self.__if_sum, self.__ordering, self.__if_desc)

    def is_key_word(self, key_word):
        return key_word in Translator.key_words
