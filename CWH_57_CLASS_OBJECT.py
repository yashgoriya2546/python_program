class persion():
    name = "yash"
    occupation = "software developer"
    age = 20
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = persion()
a.name = "Hardik"
a.occupation = "CA"
a.info()

b = persion()
b.name = "subham"
b.occupation = "Accountant"
b.info()

c = persion()
c.name = "nick"
c.occupation = "HR"
c.info()

print(type(persion))


