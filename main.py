import datetime
from dataclasses import dataclass


@dataclass
class Book:
    _name: str
    _year: int
    _isbn: str
    _price: float

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        if self.year > datetime.datetime.now().year:
            raise ValueError(f"Year of book must be <= {datetime.datetime.now().year}")
        self._year = year

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        if isbn.isnumeric() and len(isbn) == 13:
            self._isbn = isbn
        raise ValueError("ISBN must consist 13 numeric simbols")


    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price


    def age_of_book(self) -> int:
        return datetime.datetime.now().year - self._year


@dataclass
class Author:
    _full_name: str
    _bio: str
    _book_list: list[Book]

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str) -> None:
        self._full_name = full_name

    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, bio: str) -> None:
        self._bio = bio

    @property
    def book_list(self) -> list[Book]:
        return self._book_list

    @book_list.setter
    def book_list(self, book_list: list[Book]) -> None:
        self._book_list = book_list


    def add_book(self, book: Book):
        self._book_list.append(book)
