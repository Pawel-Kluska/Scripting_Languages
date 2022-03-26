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


file_op = FileOperations('Elephant', 'Monkey', 'Tiger', 'Lion', 'Horse')

try:
    file_op.read1()
    file_op.write1()
    file_op.append1()
    file_op.append2()
    file_op.read2()
except FileNotFoundError:
    print("Nieprawidlowy plik")
