class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"The name is a--> {self.name}")

class Dance:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"The Dance is a--> {self.dance}")

class DanceEmployee(Dance,Employee):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

o = DanceEmployee("Kathak","Shivani")
print(o.name)
print(o.dance)
o.show()
print(DanceEmployee.mro())