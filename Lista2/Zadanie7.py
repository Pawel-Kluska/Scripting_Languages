import time
import os

directory = input("Wprowadz ścieżkę dostępu do katalogu: ")
if not os.path.isdir(directory):
    print("Ścieżka dostępu musi być katalogiem.")
else:
    file = input("Wprowadz nazwę pliku: ")
    fullpath = os.path.join(directory, file)
    if not os.path.isfile(fullpath):
        print("Nie została wprowadzona nazwa pliku")
    else:
        print(os.path.getmtime(fullpath))
        time.localtime(os.path.getmtime(fullpath))
        print(os.path.getctime(fullpath))
        time.localtime(os.path.getmtime(fullpath))
        print(os.path.getatime(fullpath))
        time.localtime(os.path.getatime(fullpath))
        print(os.path.getsize(fullpath))
