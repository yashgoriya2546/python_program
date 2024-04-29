
s = {1,3,4,7,3,7}
print(s)

cities = {"mumbai" , "delhi" , "tokyo" , "new york" ,"ahmedabad","surat"}
cities2 = {"morbi" , "halvad" , "tokyo" , "surat"}
# print(cities.union(cities2))
# print(cities.issuperset(cities2))
# print(cities2)
# print(cities2.pop())
# print(cities2.update(cities))
# print(cities2.symmetric_difference(cities))
# cities.update(cities2)
# print(cities)
cities.intersection_update(cities2)
print(cities)
cities.update(cities2)
print(cities)
cities2.difference(cities)
print(cities2)
cities.symmetric_difference(cities2)
print(cities)