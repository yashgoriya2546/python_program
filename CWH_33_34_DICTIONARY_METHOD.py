# dec = {
#     "name":"yash",
#     "age":20,
#     "surname":"Goriya"
# }
# print(dec)
# print(dec["surname"])
# print(dec.keys())
# print(dec.values())
# print(dec["name"])
# for key in dec.keys():
#     print(f"The value corresponding to the key {key} is {dec[key]}")

info = {
    "name":"harry",
    "age":23,
    "eligable":"true"
}
print(info.items())
for key,value in info.keys():
    print(f"The value corresponding to the key {key} and value is{value} ")

# Dictionary methods

# ep1 = {122:45,22:78,786:20,99:80,212:44}
# ep2 = {222:89,11:55}
# ep1.update(ep2)
# print(ep2.items())
# print(ep1)
# # ep1.clear()
# # print(ep1)
# ep1.pop(122)
# print(ep1)
# ep1.popitem()
# print(ep1)
# del ep1[786]
# print(ep1)