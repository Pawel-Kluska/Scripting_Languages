isNotEnd = True
listOfEmails = []

while isNotEnd:
    email = input("Podaj swoj adres email\nJesli chcesz zakonczyc wpisz 'q'\n")
    if email == 'q':
        isNotEnd = False
    else:
        listOfEmails.append(email)

domains = {}

for email in listOfEmails:
    domain = (email.split("@")[1].split(".")[0])
    if domain in domains:
        domains[domain] += 1
    else:
        domains[domain] = 1

for elem, domain in domains.items():
    print("{0:8s} {1:2d}".format(elem, domain))

