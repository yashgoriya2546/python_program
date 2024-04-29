x = 10

def my_function():
    y = 5
    global x
    x = 7
    print(y)
    print(x)

my_function()
print(x)

def my_function2():
    global x
    x = 1

my_function2()
print(x)

def my_function3():
    print(x)

my_function3()
