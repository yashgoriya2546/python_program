class Employee:
    def __init__(self,name,salary,id):
        self.name = name
        self.salary = salary
        self.id = id

    def Display(self):
        print(f"The name is {self.name} and salary is {self.salary} and id {self.id}")

    @classmethod
    def from_str(cls,string):
        return cls(string.split("-")[0],string.split("-")[1],string.split("-")[2])

e1 = Employee("Haryy",40000,11)
e1.Display()
# print(e1.name)
# print(e1.salary)

# string = "karan-30000"
e2 = Employee.from_str("karan-30000-14")
print(e2.name)
print(e2.salary)
print(e2.id)
print("----------------------------------------------------------------------------------------------------")
class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def for_string(cls,str):
        return cls(str.split(",")[0],str.split(",")[1])

p1 = Persion("yash",12)
print(p1.name)
print(p1.age)

p2 = Persion.for_string("rinku,22")
print(p2.name)
print(p2.age)
