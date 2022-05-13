import configparser
import tkinter as tk
import tkinter.messagebox
from functools import partial
from tkinter import messagebox
from tkinter.constants import NSEW, RIGHT, END
import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox

from Lista8.logic import Logger
from Lista8.logic.CovidService import CovidService
from Lista8.logic.Natural_Language_Translator import Translator

dane_konfig = 'config/config.txt'


class BazoweGui(tk.Frame):
    def __init__(self, master=None):
        self.result = None
        self.log_file = None
        self.query = None
        self.covid_file = None
        self.konfig = configparser.ConfigParser()
        self.konfig.read(dane_konfig, "UTF8")
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.title('Covid App')
        self.parent.protocol("WM_DELETE_WINDOW", self.file_quit)
        domyslne = self.konfig["DEFAULT"]
        self.geometria_baza = domyslne.get('bazowa_geometria', "1000x800+50+50")
        self.parent.geometry(self.geometria_baza)
        self.utworz_bazowe_menu()
        self.utworz_pasek_narzedzi()
        self.utworz_status("Status")
        self.utworz_okno_podstawowe()
        self.dodaj_menu_help()
        self.parent.columnconfigure(0, weight=999)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)

    def utworz_pasek_narzedzi(self):
        self.toolbar_images = []  # muszą być pamiętane stale
        self.toolbar = tk.Frame(self.parent)
        for image, command, desc, shortcut in (
                ("images/covid.gif", self.covid_file_open, "Ctrl+C", "<Control-c>"),
                ("images/fileopen.gif", self.log_file_open, "Ctrl+L", "<Control-l>"),
                ("images/filenew.gif", self.utworz_okno_robocze, "Ctrl+N", "<Control-n>"),
                ("images/editedit.gif", self.utworz_okno_wyswietlajace, "Ctrl+O", "<Control-o>"),
                ("images/filesave.gif", self.file_save, "Ctrl+S", "<Control-s>")):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tkinter.Button(self.toolbar, image=image,
                                        command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)  # KOLEJNE ELEMENTY
                self.parent.bind(shortcut, command)
            except tkinter.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)

    def utworz_status(self, status):
        self.statusbar = tk.Label(self.parent, text=status,
                                  anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2,
                            sticky=tkinter.EW)

    def ustawStatusBar(self, txt):
        self.statusbar["text"] = txt

    def clearStatusBar(self):
        self.statusbar["text"] = ""

    def utworz_bazowe_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command in (
                ("New Ctrl-N", self.utworz_okno_robocze),
                ("Show Ctrl-O", self.utworz_okno_wyswietlajace()),
                ("Open Covid File Ctrl-C", self.covid_file_open),
                ("Open Logs File Ctrl-L", self.log_file_open),
                ("Save Ctrl-S", self.file_save),
                (None, None),
                ("Quit", self.file_quit)):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0)

    def dodaj_menu_help(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command in (
                ("New...", self.new_help),
                ("Show...", self.show_help),
                ("Open Covid File...", self.covid_file_help),
                ("Open Logs File...", self.log_file_help),
                ("Save", self.file_save_help),
                ("Command", self.command_help),
                (None, None),
                ("Quit", self.file_quit_help)):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command)

        self.menubar.add_cascade(label="Help", menu=fileMenu, underline=0)

    def new_help(self):
        messagebox.showinfo('Informacja', "Przycisk tworzy nowy arkusz wprowadzania")

    def show_help(self):
        messagebox.showinfo('Informacja', 'Po wciśnięciu zostaną wyświetlone wyniki wprowadzonej wcześniej komendy')

    def covid_file_help(self):
        messagebox.showinfo('Informacja', 'Służy do wybrania pliku z danymi Covidowymi')

    def log_file_help(self):
        messagebox.showinfo('Informacja', 'Służy do wybrania pliku z logami')

    def file_save_help(self):
        messagebox.showinfo('Informacja', 'Służy do zapisu wyników do plików z logami')

    def file_quit_help(self):
        messagebox.showinfo('Informacja', 'Wyjście z programu')

    def command_help(self):
        messagebox.showinfo('Informacja', 'Komendy mają następujący schemat\n\n' +
                            'show sum/list of cases/deaths in territory (for nr month)' +
                            '/ (between day1 month1 and day2 month2) order by cases/deaths/day desc/asc\n\n' +
                            'Przykład: show sum of cases in Asia for 1 April order by cases desc \n\n' +
                            'show list of deaths in Afghanistan between 1 November and 30 November order by date asc')

    def file_quit(self, event=None):
        reply = tkinter.messagebox.askyesno(
            "Zamykanie programu",
            "Czy jesteś pewien?", parent=self.parent)
        event = event
        if reply:
            geometria = self.parent.winfo_geometry()
            self.konfig["DEFAULT"]["bazowa_geometria"] = geometria
            with open(dane_konfig, 'w') as konfig_plik:
                self.konfig.write(konfig_plik)
            self.parent.destroy()

    def covid_file_open(self, event=None):
        dir = (os.path.dirname(self.covid_file)
               if self.covid_file is not None else ".")
        filename = tk.filedialog.askopenfilename(
            title="Covid file",
            initialdir=dir,
            filetypes=[("Text file", "*.txt")],
            defaultextension=".txt", parent=self.parent)
        if filename:
            self.covid_file = filename
        self.utworz_status("Covid file loaded")

    def log_file_open(self, event=None):
        dir = (os.path.dirname(self.log_file)
               if self.log_file is not None else ".")
        filename = tk.filedialog.askopenfilename(
            title="Logs file",
            initialdir=dir,
            filetypes=[("Text file", "*.txt")],
            defaultextension=".txt", parent=self.parent)
        if filename:
            self.log_file = filename
        self.utworz_status("Logs file loaded")

    def file_save(self, event=None):
        event = event
        if self.log_file is not None and self.result is not None:
            Logger.save_log(self.log_file, self.result, self.query)
            messagebox.showinfo("Info", "Zapisano pomyślnie")
        else:
            messagebox.showinfo("Info", "Nie znalezniono danych")
        self.utworz_status("Output saved")

    def utworz_okno_robocze(self):

        self.robocze = tk.Frame(self.parent, background='#0CB97F')
        label_query = tk.Label(self.robocze, text="Podaj zapytanie", font=("Arial Bold", 20), background='#0CB97F')
        label_query.place(x=30, y=50, width=200,
                          height=50)
        query_entry = tk.Entry(self.robocze, font=("Arial Bold", 20))
        query_entry.place(x=250,
                          y=50,
                          width=500,
                          height=50)
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        translator = Translator()

        def evaluate(obj):
            service = CovidService(self.covid_file)
            translator.set_service(service)
            query = query_entry.get()
            obj.query = query
            try:
                obj.result = translator.translate(query)
            except Exception:
                obj.result = 'Wprowadzono nieprawidłowe dane'
            messagebox.showinfo('Informacja', 'Dane zostały przetworzone')

        btn = tk.Button(self.robocze, text="Potwierdź", command=partial(evaluate, self))
        btn.place(x=650,
                  y=120,
                  width=100,
                  height=50)
        self.utworz_status("Command view")

    def utworz_okno_podstawowe(self):

        self.robocze = tk.Frame(self.parent, background='#0CB97F')
        label_query = tk.Label(self.robocze, text="Wybierz opcję z górnego menu", font=("Arial Bold", 20),
                               background='#0CB97F')
        label_query.place(x=150, y=50, width=400,
                          height=50)
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

    def utworz_okno_wyswietlajace(self):
        self.robocze = tk.Frame(self.parent, background='#0CB97F')
        label_query = tk.Label(self.robocze, text="Dane prezentują się następująco", font=("Arial Bold", 20),
                               background='#0CB97F')
        label_query.place(x=150, y=50, width=400,
                          height=50)

        if self.result == None:
            out = 'Nie znaleziono danych'
        else:
            out = self.result

        # Add a Scrollbar(horizontal)
        v = tk.Scrollbar(self.robocze, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        # Add a text widget
        text = tk.Text(self.robocze, font="Georgia, 24", yscrollcommand=v.set)

        text.insert(END, out + '\n')

        # Attach the scrollbar with the text widget
        v.config(command=text.yview)
        text.pack()

        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        self.utworz_status("Output view")
