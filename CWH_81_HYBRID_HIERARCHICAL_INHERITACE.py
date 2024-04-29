class University:
    def __init__(self):
        print("Construvtor of the base class")

        self.uni = "Surashtra univercity"

    def display(self):
        print(f"The University name is: {self.uni}")

class Course(University):
    def __init__(self):
        print("Constructor of the child class 1 of class university")
        University.__init__(self)
        self.Course = "information technology"

    def display(self):
        print(f"The course name is: {self.Course}")
        University.display(self)

class Branch(University):
    def __init__(self):
        print("Constructor of the child class 2 of class university")
        self.Branch = "web development"
    def display(self):
        print(f"The Branch name is: {self.Branch}")
        Course.display(self)

class Student(Course,Branch):
    def __init__(self):
        print("constructor of child class of course and branch is called")
        self.name = "Tonny"
        Branch.__init__(self)
        Course.__init__(self)

    def display(self):
        print(f"The name of the student is: {self.name}")
        Branch.display(self)
       # Course.display(self)

ob = Student()
ob.display()