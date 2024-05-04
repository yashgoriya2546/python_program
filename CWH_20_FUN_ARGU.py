# def average(a,b):
#     print("Average is:" ,(a+b)/2)
# average(6,10)
#
# def sub(c,d):
#     print("Subtraction is",c - d)
# sub(10,7)
#
# def sum(x=10 , y=10, z=10):
#     print("Sum is:", (x+y+z))
# sum(x=1,y=1,z=1)


def average(*numbers):
    print(type(average))
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)
c = average(10,40,60,80,10)
print(c)



def information(**args):
    print('The name is ' + args['name'] + ', the city is ' + args['city'] + ', and the phone number is ' + args['phone_num'])

information(name='yash', city='Morbi', phone_num='8866062681')
