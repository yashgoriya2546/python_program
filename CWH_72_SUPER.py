class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary

class Programmer(Employee):
    def __init__(self,id,name,lang,salary):
        super().__init__(name,id,salary)
        self.lang = lang

    def show(self):
        print(f"the id is {self.id} nad name is {self.name} salary is {self.salary} and language is {self.lang}")

arpit = Employee("arpit dr",435,40000)
yash = Programmer("yash patel",420,"python",80000)
yash.show()
harry = Programmer(222,"harry mod","java",22222)
harry.show()
# print(yash.name)
# print(yash.id)
# print(yash.salary)
# print(yash.lang)

class Persion:
    def super_class(self):
        print("This is a super class--> 1")

class Man(Persion):
    def super_class(self):
        print("This is a super class--> 3")
        super().super_class()
    def child_class(self):
        print("This is a child class--> 2")
        super().super_class()


a = Man()
a.child_class()
a.super_class()