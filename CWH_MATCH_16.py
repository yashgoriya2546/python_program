from unittest import case

x = (input("Enter x number: "))

match x:
    case 0:
        print("Number is Zero")
    case 1:
        print("Number is one")
    case 2:
        print("Number is a Two")
    case _ :
        print("Not matched")
