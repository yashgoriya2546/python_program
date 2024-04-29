class myclass:
    def __int__(self,value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

obj = myclass()
obj.ten_value = 67
print(obj.ten_value)
obj.show()



class p:
    def __int__(self,age = 0):
        self._age = age

        #getter method
    def get_age(self):
        return self._age * 2

        #setter method
    def set_age(self,x):
        self._age = x

yash = p()

yash.set_age(20)
print(yash.get_age())
print(yash._age)
