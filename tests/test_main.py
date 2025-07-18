import datetime

from factory import AuthorFactory, BookFactory

from app.main import (
    BookFixDiscount,
    BookPersentDiscount,
    CatalogDTO,
    LibraryCatalog,
    catalog_to_json,
)


def test_add_book() -> None:
    book = BookFactory.build()
    author = AuthorFactory.build()
    author.add_book(book)
    assert book in author.get_book_list()


def test_age_of_book() -> None:
    book = BookFactory.build(year=2020)
    assert book.age_of_book() == 5


def test_book_older_than_5_years() -> None:
    year = datetime.datetime.now().year - 6
    book = BookFactory.build(year=year)
    author = AuthorFactory.build()
    author.add_book(book)
    assert author.book_list[-1].age_of_book() > 5


def test_book_younger_than_5_years() -> None:
    year = datetime.datetime.now().year - 4
    book = BookFactory.build(year=year)
    author = AuthorFactory.build()
    author.add_book(book)
    assert author.book_list[-1].age_of_book() < 5


def test_book_zero_discount() -> None:
    book = BookFactory.build(price=20.6)
    assert book.final_price() == book.price


def test_book_fix_discount() -> None:
    book = BookFactory.build(price=200, discount=BookFixDiscount(20))
    assert book.final_price() == 180


def test_book_persent_discount() -> None:
    book = BookFactory.build(price=200, discount=BookPersentDiscount(30))
    assert book.final_price() == 140


def test_book_discount_with_different_strategy() -> None:
    book = BookFactory.build(price=100)
    book.discount = BookFixDiscount(20)
    assert book.final_price() == 80
    book.discount = BookPersentDiscount(30)
    assert book.final_price() == 70


def test_add_book_library_catalog() -> None:
    catalog = LibraryCatalog()
    book = BookFactory.build()
    catalog.add_book(book)
    assert book.isbn in catalog.books


def test_remove_book_library_catalog() -> None:
    catalog = LibraryCatalog()
    book = BookFactory.build()
    catalog.add_book(book)
    catalog.remove_book(book.isbn)
    assert book.isbn not in catalog.books


def test_search_book_library_catalog() -> None:
    catalog = LibraryCatalog()
    book = BookFactory.build()
    catalog.add_book(book)
    assert catalog.search_book(book.isbn) == book


def test_total_cost_library_catalog() -> None:
    catalog = LibraryCatalog()
    book1 = BookFactory.build(price=10)
    book2 = BookFactory.build(price=20)
    catalog.add_book(book1)
    catalog.add_book(book2)
    assert catalog.total_cost() == 30


def test_catalog_to_json() -> None:
    catalog_json = (
        "{"
        '"authors": ['
        "{"
        '"id": 1, '
        '"full_name": "Tom Black", '
        '"bio": "Good author in Poland"'
        "}"
        "], "
        '"books": ['
        "{"
        '"isbn": "1234567890123", '
        '"title": "Harry Potter", '
        '"year": 2024, "price": 20.5, '
        '"authorId": 1'
        "}"
        "]"
        "}"
    )
    catalog = CatalogDTO.model_validate_json(catalog_json)
    assert catalog == CatalogDTO.model_validate_json(catalog_to_json(catalog))
