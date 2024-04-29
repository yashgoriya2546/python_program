name = "yash"
surname = "Goriya"

print(f"My name is a {name} {surname}")

print(f"My name is a {{name}} {{surname}}") # This is a f string

def squre(n):
    '''
    This is a DOC string
    '''
    print(squre.__doc__)
    print(n*5)

squre(5)