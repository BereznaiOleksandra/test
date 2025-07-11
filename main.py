import datetime
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    year: int
    isbn: str
    price: float

    def get_title(self) -> str:
        return self.title

    def update_title(self, title: str) -> None:
        if not title:
            raise ValueError("Title can not be empty")
        self.title = title

    def get_year(self) -> int:
        return self.year

    def update_year(self, year: int) -> None:
        if self.year > datetime.datetime.now().year:
            raise ValueError(f"Year of book must be <= {datetime.datetime.now().year}")
        self.year = year

    def get_isbn(self) -> str:
        return self.isbn

    def update_isbn(self, isbn: str) -> None:
        if isbn.isnumeric() and len(isbn) == 13:
            self.isbn = isbn
        raise ValueError("ISBN must consist 13 numeric simbols")

    def get_price(self) -> float:
        return self.price

    def update_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price can not be negative")
        self.price = price


    def age_of_book(self) -> int:
        return datetime.datetime.now().year - self.year


@dataclass
class Author:
    full_name: str
    bio: str
    book_list: list[Book]

    def get_full_name(self) -> str:
        return self.full_name

    def update_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def get_bio(self) -> str:
        return self.bio

    def update_bio(self, bio: str) -> None:
        self.bio = bio

    def get_book_list(self) -> list[Book]:
        return self.book_list

    def update_book_list(self, book_list: list[Book]) -> None:
        self.book_list = book_list


    def add_book(self, book: Book):
        self.book_list.append(book)
