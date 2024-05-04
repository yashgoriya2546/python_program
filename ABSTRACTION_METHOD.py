from abc import ABC,abstractmethod

class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print('The mileage is 30kmph')

class Suzuki(Car):
    def mileage(self):
        print('The mileage is 25kmph')


class Duster(Car):
    def mileage(self):
        print('The mileage is 23kmph')


class Honda(Car):
    def mileage(self):
        print('The mileage is 27kmph')


t = Tesla()
t.mileage()


s = Suzuki()
s.mileage()

d = Duster()
d.mileage()

h = Honda()
h.mileage()