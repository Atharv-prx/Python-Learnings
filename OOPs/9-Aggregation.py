# Aggregation - Represents a relationship where one object (the whole) contains refrences to one or more INDEPENDENT objects (the parts)
class library:
    def __init__(self, name):
        self.name = name
        #containg books in library
        self.Books = []
    
    def addBook(self, Book):
        self.Books.append(Book)

    def printBook(self):
        return [f"{x.title} by {x.author}"for x in self.Books]


class books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
#Both library and book classes are independent

Library = library("Amsterdam public library")

book1 = books("Harry Poter", "J.K. Rowling")
book2 = books("Maths Class 12th", "NCERT")
book3 = books("Chemistry Class 12th", "NCERT")

Library.addBook(book1)
Library.addBook(book2)
Library.addBook(book3)

print(Library.name)
for x in Library.printBook():
    print(x)