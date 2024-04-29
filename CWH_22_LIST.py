marks = [22,44,55,34,89,"yash","true","False"]
print(marks[6])
print(marks[-3])
print(marks[len(marks)-3])
print(marks[7-3])
print(marks[-3:6])
if "yash" in marks:
    print("yes")
else:
    print("No")
if "pi" in "Arpit":
    print("yes")
else:
    print("no")

print(marks[1:8:3])

lst = [i+10 for i in range(4)]
print(lst)



print(marks.append(200))
print(marks)

list = marks.copy()
print(list)

sorting = [5,67,23,7,2,9,55,89,9]
sorting.sort(reverse=True)
print(sorting)
print(sorting.count(9))
sorting.insert(1,4)
print(sorting)
m = [900,203,666]
# sorting.extend(m)
# print(sorting)
k= sorting + m
print(k)

list = ["Hardik","yash","True","BMW"]
list2 = []

for i in list:
    for j in i:
        if j in ('a','e','i','u'):
            break
        else:
            list2.append(j)
    print(list2)