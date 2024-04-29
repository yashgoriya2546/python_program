x = [13,76,87]
print(x.__dir__())

a = 44
class Persion:
    def __init__(self,no,name):
        self.no = no
        self.name = name
        self.salary = 20000

p = Persion(1,"Rocky")
print(p.__dict__)
print(a.__dir__())

help(Persion)