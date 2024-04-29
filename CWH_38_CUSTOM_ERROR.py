a = input("enter a number between 5 to 9: ")
# if int(a)<5 or int(a)>9:
#     raise ValueError("error generate")

if (a=="quite"):
    print("ohk")
elif int(a)<5 or int(a)>9:
    raise ValueError("The number should be between 5 and 9")