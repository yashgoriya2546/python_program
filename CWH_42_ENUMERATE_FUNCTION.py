marks = [12,45,3,77,65,89,23,66]
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("yash Awesome")
#     index +=1

for index,mark in enumerate(marks,start=1):
    if index >= len(marks):
        break
    else:
     print(index,marks[index])
     if(index == 3):
        print("yash Awesome")

tup = ("yash","meet","sohil","krutik","shyam")
print(type(tup))

for i,tup in enumerate(tup,start=0):
    print(i,tup)
    if i==4:
        print("come here")