import datetime


class Access:
    def __set_name__(self, owner, name: str):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class Author:
    full_name = Access()
    bio = Access()
    book_list = Access()

    def __init__(self, full_name: str, bio: str = None, book_list: list = None):
        self.full_name = full_name
        self.bio = bio
        self.book_list = book_list

    def add_book(self, book_name: str):
        self.book_list.append(book_name)


class Book:
    name = Access()
    year = Access()
    isbn = Access()
    price = Access()

    def __init__(self, name: str, year: int, isbn: str, price: float):
        self.name = name
        self.year = year
        self.isbn = isbn
        self.price = price

    def age_of_book(self):
        return datetime.datetime.now().year - self.year

# book = Book("Book1", 2000, 1234567890, 23)
# author = Author("Tom Rick", "Writer", ["book1", "book2"])
# author.add_book("book3")
# print(author.book_list)
