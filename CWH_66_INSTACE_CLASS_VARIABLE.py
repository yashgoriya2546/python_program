class Employee:
    CompanyName = "Apple"
    NoOfEmployees = 0

    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.NoOfEmployees += 1

    def ShowDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount of {self.NoOfEmployees} sized " 
              f"{self.CompanyName} is {self.raise_amount} ")


emp1 = Employee("Yash")
emp1.raise_amount = 0.3
emp1.CompanyName = "Tesla"
emp1.ShowDetails()

Employee.CompanyName = "Google"
print(Employee.CompanyName)

emp2 = Employee("Arpit")
emp2.ShowDetails()