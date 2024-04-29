def fib(limit):
    a,b = 0,1

    while a < limit:
        yield a
        a,b = b, a+b

x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

def lst():
    lis = ["apple","banana","orange"]
    for i in lis:
        yield i


l = lst()
print(next(l))
print(next(l))
print(next(l))

squares_generator = (i * i for i in range(5))

for i in squares_generator:
    print(i)
