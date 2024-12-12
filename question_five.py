#5(i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

book = Book("Who saw my soul", "Coleen Hoover", 360)
print(book.info())

#5(ii)
class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def information(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.format}"

ebook = EBook("Who saw my soul", "Coleen Hoover", 360, "Epub")
print(ebook.information())


#5(iii)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

book = Book("Who saw my soul", "Coleen Hoover")
print(book.title_and_author())

#5(iv)
#Class: A class is a blueprint for creating objects in object-oriented programming.

#Object: An object is an instance of a class. 