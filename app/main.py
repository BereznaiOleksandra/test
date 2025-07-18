import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Annotated

from pydantic import AfterValidator, BaseModel


class AbstractPriceDiscount(ABC):
    def __init__(self, discount: float = 0):
        self.discount = discount

    @abstractmethod
    def apply(self, price: float) -> float:
        pass


class BookZeroDiscount(AbstractPriceDiscount):
    def apply(self, price: float) -> float:
        return price


class BookFixDiscount(AbstractPriceDiscount):
    def apply(self, price: float) -> float:
        return price - self.discount


class BookPersentDiscount(AbstractPriceDiscount):
    def apply(self, price: float) -> float:
        return price - self.discount * price / 100


@dataclass
class Book:
    title: str
    year: int
    isbn: str
    price: float
    discount: AbstractPriceDiscount = BookZeroDiscount()

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

    def final_price(self) -> float:
        return self.discount.apply(self.price)


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

    def add_book(self, book: Book) -> None:
        self.book_list.append(book)


class LibraryCatalog:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    def remove_book(self, isbn: str) -> bool:
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def search_book(self, isbn: str) -> Book | None:
        return self.books.get(isbn)

    def total_cost(self) -> float:
        return sum(book.price for book in self.books.values())


class AuthorDTO(BaseModel):
    id: int
    full_name: str
    bio: str


def check_isbn(value: str) -> str:
    if not value.isnumeric() or len(value) != 13:
        raise ValueError("ISBN must consist 13 numeric simbols")
    return value


def check_year(value: int) -> int:
    if value < 0 or value > datetime.datetime.now().year:
        raise ValueError(f"Year of book must be <= {datetime.datetime.now().year}")
    return value


class BookDTO(BaseModel):
    isbn: Annotated[str, AfterValidator(check_isbn)]
    title: str
    year: Annotated[int, AfterValidator(check_year)]
    price: float
    authorId: int


class CatalogDTO(BaseModel):
    authors: list[AuthorDTO]
    books: list[BookDTO]


def catalog_to_json(catalog: CatalogDTO) -> str:
    return catalog.model_dump_json(indent=2)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
