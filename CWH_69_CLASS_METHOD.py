class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def Changecompany(cls,changecompany):
        cls.company = changecompany


e = Employee()
e.name = "Yash"
e.show()
e.Changecompany("Microsoft")
e.show()
e2 = Employee()
e2.name = "Shubham"
e2.Changecompany("TATA")
e2.show()