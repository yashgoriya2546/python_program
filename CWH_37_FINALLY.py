def func1():
 try:
    a = int(input("Enter a index "))
    arr = [1,4,7,2,3]
    print(arr[a])
    return 1
 except Exception as e:
     print(e)
     return 0

 finally:
     print("i always executed")


x = func1()
print(x)