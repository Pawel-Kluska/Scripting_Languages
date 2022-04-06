
class FileOperations:
    filename = 'data.txt'
    line = 'Animals:'

    def __init__(self, *args):
        self.species = args

    def write1(self):
        with open(FileOperations.filename, 'w') as file:
            file.write(FileOperations.line + "\n")
            for animal in self.species:
                file.write(animal + '\n')

    def read1(self):
        with open(FileOperations.filename, 'r') as file:
            for line in file:
                print(line.strip() + " ", end='')

    def append1(self):
        with open(FileOperations.filename, 'a') as file:
            file.write('\n')
            file.write("Tu bedzie strona internetowa")

    def append2(self):
        with open(FileOperations.filename, 'a') as file:
            file.write('\n')
            file.write(input("Podaj swoja ulubiona strone internetowa"))

    def read2(self):
        with open(FileOperations.filename, 'r') as file:
            for line in file:
                print(line)

    def species(self):
        print('Getting...')
        return self.species

    def set_species(self, value):
        if isinstance(value, list):
            if value is not []:
                self.species = value
            else:
                raise TypeError('The price attribute must be positive.')
        else:
            raise ValueError('The price attribute must be an int or float value.')

    def del_species(self):
        del self.species

    price = property(fget=species, fset=set_species, fdel=del_species)


file_op = FileOperations('Elephant', 'Monkey', 'Tiger', 'Lion', 'Horse')

try:
    file_op.read1()
    file_op.write1()
    file_op.append1()
    file_op.append2()
    file_op.read2()
except FileNotFoundError:
    print("Nieprawidlowy plik")

file_op.set_species(["siema"])
print(file_op.species);
