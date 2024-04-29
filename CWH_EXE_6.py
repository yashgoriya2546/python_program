class Library:
    def __init__(self):
        self.books = []
        self.no_of_book = 0

    def addbook(self,book):
        self.books.append(book)
        self.no_of_book = len(self.books)

    def showbook(self):
        print(f"no of books are {self.no_of_book} and books are available are")
        for i in enumerate(self.books,start=1):
            print(i)

l1 = Library()
l1.addbook("Mahabharat")
l1.addbook("Ramayan")
l1.addbook("Shrimadbhagvatgeeta")
l1.showbook()