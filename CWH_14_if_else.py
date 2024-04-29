a = int(input("Enter your number: "))
if (a>=18):
    print("You can drive")
else:
    print("You can not drive")

num = int(input("Enter your Number=> "))

if(num >= 0):
    if(num>=0 and num<=10):
        print("num is a between 0 and 10")
    elif(num >=20 and num<=50):
        print("num is a between 20 and 50")
    elif(num >= 50):
        print("num is a up to 50")
    else:("num is a Zero")


# num = 1
#
# if(num<=10):
#     for i in range(1,10):
#         print(num * i)

year = int(input("Enter your Year"))
if year % 4 == 0:
    print("Yes This is a leap year")
else:
    print("This is a not leap year")

print(id(year))