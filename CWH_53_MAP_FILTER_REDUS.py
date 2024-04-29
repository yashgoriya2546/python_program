def cube(x):
    return x*x*x

def cube2(x):
    return x>=4


l = [1,2,5,43,56,12]

newl = list(map(cube,l))
print(newl)

fnew = tuple(filter(cube2,l))
print(fnew)

from functools import reduce

rnew = reduce(lambda x,y:x + y,l)
print(rnew)