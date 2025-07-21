import datetime
import json
import pathlib

import pytest
from pydantic import ValidationError

from app.main import (
    BookFixDiscount,
    BookPersentDiscount,
    CatalogDTO,
    LibraryCatalog,
    catalog_to_json,
)
from factories import AuthorFactory, BookDTOFactory, BookFactory, CatalogDTOFactory


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
    catalog_json = json.loads(pathlib.Path("data_for_test.json").read_text())
    catalog = CatalogDTO(**catalog_json)
    assert catalog == CatalogDTO(**json.loads(catalog_to_json(catalog)))


def test_dto_validation_error() -> None:
    bad_book = BookDTOFactory.build(
        isbn="123456",
        factory_use_construct=True,
    )
    catalog = CatalogDTOFactory.build(books=[bad_book])
    catalog_json = json.loads(catalog_to_json(catalog))

    with pytest.raises(ValidationError) as exc_info:
        CatalogDTO(**catalog_json)

    assert "ISBN must consist 13 numeric simbols" in str(exc_info.value)
