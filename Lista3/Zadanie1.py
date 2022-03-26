def get_email_array():
    is_not_end = True
    list_of_emails = []

    while is_not_end:
        email = input("Podaj swoj adres email\nJesli chcesz zakonczyc wpisz 'q'\n")
        if email == 'q':
            is_not_end = False
        else:
            list_of_emails.append(email)
    return list_of_emails


def get_domains_list(list_of_emails):
    domains = {}

    for email in list_of_emails:
        try:
            domain = (email.split("@")[1].split(".")[0])
        except IndexError:
            print("Podano nieprawidlowe dane, ominieto ten email: " + domain)
            continue

        if domain in domains:
            domains[domain] += 1
        else:
            domains[domain] = 1
    return domains


def print_elem(domains):
    for elem, domain in domains.items():
        print("{0:8s} {1:2d}".format(elem, domain))


user_array = get_email_array()
domains_list = get_domains_list(user_array)
print_elem(domains_list)
