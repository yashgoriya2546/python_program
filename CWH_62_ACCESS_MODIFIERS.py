# class Employee:
#     def __init__(self):
#         self.__name = "Harry2"
#
# a = Employee()
# # print(a.__name) can not be accesed directly
# print(a._Employee__name)  # can be accessed indirectly
# print(a.__dir__())

class Student:
    def __init__(self):
        self._name = "Yash"

    def _funname(self):
        return "Code with Harry"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funname())

print(obj1._name)
print(obj1._funname())
print(obj.__dir__())