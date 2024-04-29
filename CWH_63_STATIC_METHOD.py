class Persion:
    def __init__(self):
        self.num = 0  # Initialize num attribute upon object creation

    def sum(self, n, num):  # Add num as a parameter to the sum method
        self.num = num  # Store the value of num as an attribute
        return self.num + n
    @staticmethod
    def add(a,b):
        return a + b

x = Persion()
result = x.sum(10,2)
print(result)
print(Persion.add(10,10))