class Employee:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i = 0
        for j in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name is {self.name}"

    def __repr__(self):
        return "This is repr method"

    def __call__(self):
        for i in range(5):
            for j in range(i+1):
                print("* ",end=" ")
            print()

        for k in range(5, 0, -1):
            for r in range(0, k - 1):
                print("* ", end=" ")
            print()

        for v in range(1,5+1):
            for d in range(v):
                print(v,end=" ")
            print()