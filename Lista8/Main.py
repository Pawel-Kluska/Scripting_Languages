import tkinter as tk

from Lista8.gui.szablon_gui import BazoweGui

if __name__ == '__main__':
    root = tk.Tk()

    app = BazoweGui(master=root)
    app.mainloop()