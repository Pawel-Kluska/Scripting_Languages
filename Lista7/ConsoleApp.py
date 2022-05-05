import os

import CovidService
import Natural_Language_Translator
from Lista7 import Logger


class ConsoleApp:

    def __init__(self):
        self.__file_input = None
        self.__file_output = None
        self.__query = None

    def start_console_app(self):
        translator = Natural_Language_Translator.Translator()
        while True:
            self.__file_input = ConsoleApp.get_string('Podaj nazwe pliku do zczytania danych',
                                                      default=self.__file_input)
            self.__file_output = ConsoleApp.get_string('Podaj nazwe pliku do zapisania logow',
                                                       default=self.__file_output)
            if os.path.exists(self.__file_input) and os.path.exists(self.__file_output):
                service = CovidService.CovidService(self.__file_input)
                translator.set_service(service)

                self.__query = ConsoleApp.get_string('Podaj zapytanie', default=self.__query)
                respond = translator.translate(self.__query)
                print(respond)
                Logger.save_log(self.__file_output, respond, self.__query)
            else:
                print("No such file")

    @staticmethod
    def get_string(message, name="string", default=None,
                   minimum_length=0, maximum_length=80,
                   force_lower=False):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line:
                    if default is not None:
                        return default
                    if minimum_length == 0:
                        return ""
                    else:
                        raise ValueError("{0} may not be empty".format(
                            name))
                if not (minimum_length <= len(line) <= maximum_length):
                    raise ValueError("{0} must have at least {1} and "
                                     "at most {2} characters".format(name, minimum_length, maximum_length))
                return line if not force_lower else line.lower()
            except ValueError as err:
                print("ERROR", err)


if __name__ == '__main__':
    console = ConsoleApp()
    console.start_console_app()
