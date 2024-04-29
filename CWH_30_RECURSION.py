def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * factorial(n-1)
print(factorial(5))


# f0 = 0
# f1 = 1
# for i in range(5):
#     f2 = f1 + f0
#     print(f2)
#
#     f0 = f1
#     f1 = f2


# fibonacci series using recursion

# def fibonacci(n):
#     if n<= 1:
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
# term = 10
#
# for i in range(term):
#     print(fibonacci(i))

def prime(n):
    if n>6:
        return n
    else:
     print(n)
     prime(n+1)
prime(1)

