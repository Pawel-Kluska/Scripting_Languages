class Employee:
    amount_of_objects = 0

    def __init__(self, name, surname, email, address, monthly_earnings):
        self.name = name
        self.surname = surname
        self.email = email
        self.address = address
        self.monthly_earnings = monthly_earnings
        Employee.amount_of_objects += 1

    def year_earnings(self):
        return self.monthly_earnings * 12

    def show(self):
        for key, value in self.__dict__.items():
            print(key + " " + str(value))


e1 = Employee("Pawel", "Kluska", "pk@gmail.com", "Wroclaw", 8000)
e2 = Employee("Jan", "Nowak", "jn@gmail.com", "Wroclaw", 3000)

e1.show()
print(e2.year_earnings())

print(Employee.amount_of_objects)
