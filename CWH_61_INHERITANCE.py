class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Employee id is {self.id} and name is {self.name}")


e = Employee('subham', 122)
e.show()
e2 = Employee('Gaurav', 111)
e2.show()

class Programmer(Employee):
    def info(self):
        print('show the information')

p = Programmer('Yash',34)
p.show()
p.info()
