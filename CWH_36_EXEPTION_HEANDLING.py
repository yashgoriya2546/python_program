# a = int(input("enter your number: "))
#
# print(f"print a {a} tables")
# try:
#     for i in range(1,11):
#         print(f"{a} * {i} = {a*i}")
# except Exception as e:
#     print(e)
#
#
#
# print("Code is complete")

# Many types Error are in python

try:
    a = int(input("enter your number: "))
    c = [6, 8]
    if a >= len(c):
      print("index out of range")
    else:
     print(c[a])
except ValueError:
      print("number is not integer")

print("code complete")