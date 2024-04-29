tup = (1,67,3,45,2,78,5)
print(type(tup),tup)
print(tup[0])
print(tup[6])

# tuple are can not be change
# list are can be change

if 67 in tup:
    print("Yes 67 in a tuple")

tup2 = tup[1:6]
print(tup2)

contries = ("India","America","Itly","Africa","Japan","Canada","Russia")
print(contries)

temp = list(contries)
print(temp)

print(temp.append("Germany"))
print(temp.pop(3))
print(temp)
contries = tuple(temp)
print(tup.count(3))
print(contries)

