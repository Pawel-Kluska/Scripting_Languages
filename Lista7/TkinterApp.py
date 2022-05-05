import os
from tkinter import *
from tkinter import messagebox

from Lista7.CovidService import CovidService
from Natural_Language_Translator import Translator
from Lista7 import Logger


def start_gui():
    window = Tk()
    translator = Translator()

    window.title("Aplikacja covidowa")
    window.geometry('650x400')

    label_file = Label(window, text='Aplikacja covidowa', font=("Arial Bold", 20))
    label_file.grid(column=0, row=0)
    label_input = Label(window, text="Podaj nazwe pliku z danymi")
    label_input.grid(column=0, row=1)
    input_entry = Entry(window, width=30)
    input_entry.grid(column=1, row=1)

    label_output = Label(window, text="Podaj nazwe pliku do logow")
    label_output.grid(column=0, row=2)
    output_entry = Entry(window, width=30)
    output_entry.grid(column=1, row=2)

    label_query = Label(window, text="Podaj zapytanie")
    label_query.grid(column=0, row=3)
    query_entry = Entry(window, width=30)
    query_entry.grid(column=1, row=3)

    def evaluate():
        if os.path.exists(input_entry.get()) and os.path.exists(output_entry.get()):
            service = CovidService(input_entry.get())
            translator.set_service(service)
            output_ = output_entry.get()
            query = query_entry.get()

            respond = translator.translate(query)
            Logger.save_log(output_, respond, query)
        else:
            respond = 'No such file'

        messagebox.showinfo('Informacja', respond)


    ##########################################################

    btn = Button(window, text="Potwierdź", command=evaluate)
    btn.grid(column=3, row=4)

    window.mainloop()


if __name__ == '__main__':
    start_gui()
