is_not_ending = True

print("Witamy na Politechnice Wroclawskiej")
print("Prosimy o wpisanie swoich danych osobowych")

list_of_names = []
list_of_surnames = []
list_of_emails = []
domain = "pwr.edu.pl"

while(is_not_ending):
    name = input("Podaj swoje imie: ")
    surname = input("Podaj swoje nazwisko")
    list_of_names.append(name)
    list_of_surnames.append(surname)
    list_of_emails.append("{}.{}@{}".format(name, surname, domain))
    if input("Czy chcesz wyjsc z programu? (Wpisz q)") == 'q':
        is_not_ending = False

for i in range(len(list_of_names)):
    print("{0:10s} {1:10s} {2:20s}".format(list_of_names[i], list_of_surnames[i], list_of_emails[i]))